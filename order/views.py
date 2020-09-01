import json

from django.views     import View
from django.http      import JsonResponse, HttpResponse
from django.db.models import F, Sum

from .models          import ShoppingBag
from product.models   import Product
from user.models      import User
from user.utils       import login_confirm

class ShoppingList(View):
    @login_confirm
    def post(self, request):
        data           = json.loads(request.body)
        product        = data['product_id']
        shoppingbag, _ = ShoppingBag.objects.prefetch_related('product').get_or_create(
            user       = request.account,
            product    = Product.objects.get(id = product)
        )
        shoppingbag.quantity    += 1
        shoppingbag.total_price  = shoppingbag.quantity * shoppingbag.product.price
        shoppingbag.save()
        return JsonResponse({"message":"success"}, status = 200)

    @login_confirm
    def get(self, request):
        products     = request.GET.getlist('product_id', None)

        shoppingbag = ShoppingBag.objects.prefetch_related('product').filter(
            user = request.account
        ).annotate(
            name    = F('product__name'),
            price   = F('total_price'),
            image   = F('product__main_image')
        )
        if products: shoppingbag = shoppingbag.filter(product__id__in = products)
        shoppingbag = list(shoppingbag.values('id', 'name', 'image', 'quantity', 'price'))

        total_price = ShoppingBag.objects.aggregate(total_price = Sum('total_price'))
        if total_price['total_price'] < 50000: total_price['total_price'] += 2500

        shoppingbag.append(total_price)
        return JsonResponse({'shoppingbag':shoppingbag}, status = 200)

    @login_confirm
    def patch(self, request):
        product      = request.GET.get('product_id', None)
        is_increased = request.GET.get('is_increased', None)
        is_decreased = request.GET.get('is_decreased', None) 
        shoppingbag  = ShoppingBag.objects.prefetch_related('user', 'product').filter(
            user = request.account
        ).get(id = product)

        if is_increased:
            shoppingbag.quantity += 1
            shoppingbag.save()
        if is_decreased:
            shoppingbag.quantity -= 1
            shoppingbag.save()

        if shoppingbag.quantity == 0: shoppingbag.delete()

        shoppingbag.total_price = shoppingbag.quantity * shoppingbag.product.price
        shoppingbag.save()

        shoppingbag = list(ShoppingBag.objects.prefetch_related('product').filter(
            user = request.account
        ).annotate(
            name    = F('product__name'),
            price   = F('total_price'),
            image   = F('product__main_image')
            ).values('id', 'name', 'image', 'quantity', 'price')
        )

        total_price = ShoppingBag.objects.aggregate(total_price = Sum('total_price'))
        if total_price['total_price'] < 50000: total_price['total_price'] += 2500

        shoppingbag.append(total_price)
        return JsonResponse({'shoppingbag':shoppingbag, 'total_price':total_price['total_price']}, status = 200)

    @login_confirm
    def delete(self, request):
        data = json.loads(request.body)
        products = data['product_id']
        if products:
            shoppingbag = ShoppingBag.objects.filter(id__in = products).delete()
            print(shoppingbag)
        
        shoppingbag = list(ShoppingBag.objects.prefetch_related('product').filter(
            user = request.account
        ).annotate(
            name    = F('product__name'),
            price   = F('total_price'),
            image   = F('product__main_image')
            ).values('id', 'name', 'image', 'quantity', 'price')
        )

        total_price = ShoppingBag.objects.aggregate(total_price = Sum('total_price'))
        if total_price['total_price'] < 50000: total_price['total_price'] += 2500

        shoppingbag.append(total_price)
        return JsonResponse({'shoppingbag':shoppingbag, 'total_price':total_price['total_price']}, status = 200)

