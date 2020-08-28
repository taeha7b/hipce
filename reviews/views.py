import bcrypt, json, jwt, re

from django.views    import View
from django.http     import JsonResponse

from user.utils      import login_confirm
from .models         import Review, ReviewImage, ReviewReply
from user.models     import User
from product.models  import Product

class ReviewView(View):
    def get(self, request, id):
        try:
            # data    = json.loads(request.body)
            reviews = Review.objects.filter(product_id = id).prefetch_related('reviewimage_set')
            # reviews = Review.objects.filter(product_id = data['product_id']).prefetch_related('reviewimage_set')
            results = []
            for review in reviews:
                image_list = []
                for images in review.reviewimage_set.all():                
                    image_list.append(images.image)
                    results.append({
                    'user_id'        : review.user_id,
                    'review_id'      : review.id,
                    'content'        : review.content,
                    'product_id'     : review.product_id,
                    'review_images'  : image_list
                })
            return JsonResponse({'Review': results}, status = 200) 
        except json.decoder.JSONDecodeError:
            return JsonResponse({"MESSAGE": "JSONDecodeError"}, status = 401)

    @login_confirm
    def post(self, request):
        try:
            data    = json.loads(request.body)
            review  = Review.objects.create(
                user     = request.account,
                product  = Product.objects.get(id = data['product_id']),
                content  = data['content'],
                scroe    = data['score']
            )
            review_iamge = ReviewImage.objects.create(
                review  = review,
                image   = data['image']
            )
            return JsonResponse({"MESSAGE": "SUCCESS"}, status = 200)
            
        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status = 400)

    @login_confirm
    def put(self, request):
        try:
            data       = json.loads(request.body)
            user_id    = request.account.id
            review_id  = data['review_id']
            modification_review = Review.objects.get(
                user  = user_id,
                id    = review_id
            )
            modification_review.content = data['content']
            modification_review.save()

            if data['image']: 
                review_image_id = ReviewImage.objects.get(id=data['review_image_id'])

                modification_review_image = ReviewImage.objects.get(
                    review  = review_id,
                    id      = review_image_id
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
            Review.objects.filter(id = int(data['review_id'])).delete()
            return JsonResponse({"MESSAGE": "Review was deleted"}, status = 200)

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status = 400)

class ReviewReplyView(View):
    def get(self, request, id):
        try:
            results = []
            review_replys = ReviewReply.objects.filter(review_id = id)   

            for review_reply in review_replys:
                results.append({
                    'user_id'          : review_reply.user_id,
                    'review_reply_id'  : review_reply.id,
                    'comment'          : review_reply.comment
                })
            return JsonResponse({'Review_Reply': results}, status = 200)
    
        except json.decoder.JSONDecodeError:
            return JsonResponse({"MESSAGE": "JSONDecodeError"}, status = 401)

    @login_confirm
    def post(self, request):
        try:
            data = json.loads(request.body)
            ReviewReply.objects.create(
                user     = request.account,
                review   = Review.objects.get(id = data['review_id']),
                comment  = data['comment']
            )
            return JsonResponse({"MESSAGE": "SUCCESS"}, status = 200)
  
        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status = 400)

    @login_confirm
    def put(self, request):
        try:
            data        = json.loads(request.body)
            user_id     = request.account.id
            comment_id  = data['comment_id']
            modification_review_reply = ReviewReply.objects.get(
                user  = user_id,
                id    = comment_id
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