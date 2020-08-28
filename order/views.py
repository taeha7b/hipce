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
    def post(self, request, product_id: int):
        shoppingbag, _ = ShoppingBag.objects.prefetch_related('product').get_or_create(
            user       = request.account,
            product    = Product.objects.get(id = product_id)
        )
        shoppingbag.quantity    += 1
        shoppingbag.total_price  = shoppingbag.quantity * shoppingbag.product.price
        return HttpResponse(status = 200)

    @login_confirm
    def get(self, request):
        product     = dict(reqeust.GET.items())
        shoppingbag = list(ShoppingBag.objects.prefetch_related('product').filter(**product).annotate(
            name    = F('product__name'),
            price   = F('total_price'),
            image   = F('product__main_image')).values(
                'name', 'image', 'quantity', 'price'
            )
        )
        total_price = ShoppingBag.objects.aggregate(total_price = Sum('total_price'))

        if total_price < 50000: total_price += 2500

        shoppingbag.append(total_price)
        return JsonResponse({'shoppingbag':shoppingbag}, status = 200)

    @login_confirm
    def patch(self, request):
        product     = request.UPDATE.get('product_id', None)
        is_added    = request.UPDATE.get('is_added', None)
        shoppingbag = ShoppingBag.objects.get(product__id = product)

        if is_added: shoppingbag.quantity += 1
        else: shoppingbag.quantity        -= 1

        if shoppingbag.quantity == 0: shoppingbag.delete()

        shoppingbag.total_price = shoppingbag.quantity * shoppingbag.product.price
        shoppingbag.save()
        return HttpResponse(stauts = 200)

    @login_confirm
    def delete(self, request):
        product     = dict(request.DELETE.items())
        shoppingbag = ShoppingBag.objects.filter(**product)

        if product: shoppingbag.delete()
        return HttpResponse(status = 200)
