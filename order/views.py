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

        shoppingbag = ShoppingBag.objects.prefetch_related('product').annotate(
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
        product      = request.UPDATE.get('product_id', None)
        is_increased = request.UPDATE.get('is_increased', None)
        is_decreased = request.UPDATE.get('is_decreased', None) 
        shoppingbag  = ShoppingBag.objects.get(product__id = product)

        if is_increased: shoppingbag.quantity += 1
        if is_decreased: shoppingbag.quantity -= 1

        if shoppingbag.quantity == 0: shoppingbag.delete()

        shoppingbag.total_price = shoppingbag.quantity * shoppingbag.product.price
        shoppingbag.save()

        shoppingbag = list(ShoppingBag.objects.prefetch_related('product').annotate(
            name    = F('product__name'),
            price   = F('total_price'),
            image   = F('product__main_image')
            ).values('name', 'image', 'quantity', 'price')
        )

        total_price = ShoppingBag.objects.aggregate(total_price = Sum('total_price'))
        if total_price['total_price'] < 50000: total_price['total_price'] += 2500

        shoppingbag.append(total_price)
        return JsonResponse({'shoppingbag':shoppingbag}, status = 200)

    @login_confirm
    def delete(self, request):
        product = request.DELETE.getlist('product', None)
        if product:
            ShoppingBag.objects.filter(product__id__in = product).delete()
        
        shoppingbag = list(ShoppingBag.objects.prefetch_related('product').annotate(
            name    = F('product__name'),
            price   = F('total_price'),
            image   = F('product__main_image')
            ).values('name', 'image', 'quantity', 'price')
        )

        total_price = ShoppingBag.objects.aggregate(total_price = Sum('total_price'))
        if total_price < 50000: total_price += 2500

        shoppingbag.append(total_price)
        return JsonResponse({'shoppingbag':shoppingbag}, status = 200)
