import bcrypt, json, jwt, re

from django.views    import View
from django.http     import JsonResponse

from user.utils      import login_confirm
from .models         import Review, ReviewImage, ReviewReply
from user.models     import User
from product.models  import Product

class Review(View):
    def get(self, request):
        try:
            review = list(Review.objects.values(), ReviewImage.objects.image())
            return JsonResponse({'Review':review}, status = 200)
        
        except json.decoder.JSONDecodeError:
            return JsonResponse({"MESSAGE": "JSONDecodeError"}, status = 401)

    @login_confirm
    def post(self, request):
        try:
            data = json.loads(request.body)
            review = Review(
                user     = request.account,
                product  = Product.objects.get(name = data['name']),
                content  = data['content'],
                score    = data['score']
            )
            review.save()
            
            review_iamge = ReviewImage(
                review  = review,
                image   = data['image']
            )
            review_iamge.save()
            return JsonResponse({"MESSAGE": "SUCCESS"}, status = 200)
            
        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status = 400)

    @login_confirm
    def put(self, request):
        try:
            data = json.loads(request.body)
            user_id = request.account.id
            review_id = data['review_id']
            modification_review = Review.objects.get(
                user = user_id, 
                id = review_id
            )
            modification_review.content = data['content']
            modification_review.save()

            if not data['image'] == '': 
                review_image_id = data['review_image_id']

                modification_review_image = ReviewImage.objects.get(
                    review = review_id, 
                    id = review_image_id
                )
                modification_review_image = data['image']
                modification_review_image.save()
            pass
            
        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status = 400)
        
        except json.decoder.JSONDecodeError:
            return JsonResponse({"MESSAGE": "JSONDecodeError"}, status = 401)
    
    @login_confirm
    def delete(self, request):
        try:
            data = json.loads(request.body)
            Review.objects.get(id = data['id']).delete()
            return JsonResponse({"MESSAGE": "Review was deleted"}, status = 200)

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status = 400)

class ReviewReputation(View):
    @login_confirm
    def post(self, request):
        try:
            data     = json.loads(request.body)
            like     = 0
            dislike  = 0
            if data['like'] == True:
                like += 1
            elif data['like'] == False:
                like -= 1
            if data['dislike'] == True:
                dislike -= 1
            elif data['dislike'] == False:
                dislike += 1

            review_reputation = ReviewReputation(
                review   = Review.objects.get(user = data['name']),
                like     = like,
                dislike  = dislike,
                total    = like + dislike
            )
            review_reputation.save()

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status = 400)
        
        except json.decoder.JSONDecodeError:
            return JsonResponse({"MESSAGE": "JSONDecodeError"}, status = 401)

    def get(self, request):
        try:
            review_reputation = list(ReviewReputation.objects.values())
            return JsonResponse({'Review_Reputation':review_reputation}, status = 200)
        
        except json.decoder.JSONDecodeError:
            return JsonResponse({"MESSAGE": "JSONDecodeError"}, status = 401)

class ReviewReply(View):
    def get(self, request):
        try:
            review_reply = list(ReviewReply.objects.values())
            return JsonResponse({'Review_Reply':review_reply}, status = 200)
        
        except json.decoder.JSONDecodeError:
            return JsonResponse({"MESSAGE": "JSONDecodeError"}, status = 401)

    @login_confirm
    def post(self, request):
        try:
            data = json.loads(request.body)
            review_reply = ReviewReply(
                user     = request.account,
                review  = data['review_id'],
                comment  = data['comment']
            )
            review_reply.save()
            
        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status = 400)

    @login_confirm
    def put(self, request):
        try:
            data = json.loads(request.body)
            user_id = request.account.id
            comment_id = data['comment_id']
            modification_review_reply = ReviewReply.objects.get(
                user = user_id, 
                id = comment_id
            )
            modification_review_reply.comment = data['comment']
            modification_review_reply.save()

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status = 400)
        
        except json.decoder.JSONDecodeError:
            return JsonResponse({"MESSAGE": "JSONDecodeError"}, status = 401)
    
    @login_confirm
    def delete(self, request):
        try:
            data = json.loads(request.body)
            ReviewReply.objects.get(id = data['comment_id']).delete()
            return JsonResponse({"MESSAGE": "ReviewReply was deleted"}, status = 200)

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status = 400)