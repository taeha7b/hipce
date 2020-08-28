import json

from django.views     import View
from django.http      import JsonResponse

from .models          import Category, Product, Color, Collection

class CategoryView(View):
    def get(self, request):
        return JsonResponse(
            {'categories':list(Category.objects.values('name', 'image'))},
            status = 200
        )

class ProductsView(View):
    def get(self, request):
        keyword  = request.GET.get('keyword', None)
        category = request.GET.get('category', None)
        tag      = request.GET.get('tag', None)
        colors   = request.GET.getlist('color', None)

        products = Product.objects.prefetch_related('color', 'tag')

        if keyword:
            products = products.filter(name__icontains = keyword)
            return JsonResponse(
                {'products':list(products.values('name', 'main_image', 'sub_image', 'price', 'tag__image'))},
                status = 200
            )

        if tag:
            products = products.filter(tag__name = tag)
            return JsonResponse({'products':list(products.values('name', 'main_image'))}, status = 200)
        
        products = products.filter(category__name = category)

        if colors:
            products = products.filter(color__name__in = colors)

        return JsonResponse(
            {'products':list(products.values('name', 'main_image', 'sub_image', 'price', 'tag__image'))},
            status = 200
        )

class ProductView(View):
    def get(self, request, product_id):
        product = Product.objects.filter(id = product_id).values(
            'id', 'name', 'main_image', 'description_image', 'price'
        )
        return JsonResponse(
            {'product':list(product)},
            status = 200
        )

class ColorsView(View):
    def get(self, request):
        return JsonResponse(
            {'colors':list(Color.objects.values('name'))},
            status = 200
        )

class CollectionsView(View):
    def get(self, request):
        return JsonResponse(
            {'collection':list(Collection.objects.values('name', 'image'))},
            status = 200
        )