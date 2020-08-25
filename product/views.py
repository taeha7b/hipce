import json

from django.views import View
from django.http  import JsonResponse

from .models      import Category, Product, Color

class CategoryView(View):
    def get(self, request):
        ''' 만든 이: 이태현
        최종 수정: 2020. 08. 25.
        정보: Shop 페이지 카테고리 이름 및 이미지 정보를 보내주는 GET방식 함수
        설명
        - 프론트 엔드에 정보만 전달하면 되고 키, 밸류로 값을 사용하기 때문에 values 쿼리셋 사용'''
        categories = Category.objects.values('name', 'image')
        return JsonResponse(
            {'categories':list(categories)},
            status = 200
        )

class ProductsView(View):
    def get(self, request):
        ''' 만든 이: 이태현
        최종 수정: 2020. 08. 25.
        정보: Shop 페이지 카테고리 별 상품 이름 및 이미지 정보를 보내주는 GET방식 함수
        설명
        - 카테고리를 기준으로 필터해주기 위해 쿼리 스트링 사용
        - 프론트 엔드에 정보만 전달하면 되고 키, 밸류로 값을 사용하기 때문에 values 쿼리셋 사용'''
        category_name = request.GET.get('category', None)
        colors_list   = request.GET.getlist('color', None)
        category_id   = Category.objects.get(name = category_name).id
        colors = Color.objects.filter('co')
        products      = Product.objects.filter(category = category_id).values(
            'name', 'main_image', 'sub_image', 'price', 'tag'
        )
        return JsonResponse(
            {'products':list(products)},
            status = 200
        )

class ProductView(View):
    def get(self, request, id):
        ''' 만든 이: 이태현
        최종 수정: 2020. 08. 25.
        정보: Shop 페이지 각 상품 상세 페이지 정보를 보내주는 GET방식 함수
        설명
        - 프론트 엔드에 정보만 전달하면 되고 키, 밸류로 값을 사용하기 때문에 values 쿼리셋 사용'''
        product = Product.objects.filter(id = id).values(
            'name', 'main_image', 'description_image', 'price'
        )
        return JsonResponse(
            {'product':list(product)},
            status = 200
        )

class ColorView(View):
    def get(self, request):
        colors = Color.objects.values('name')
        return JsonResponse(
            {'colors':list(colors)},
            status = 200
        )

class ColorFilterView(View):
    def get(self, request):
        color_name = request.GET.get('color', None)
        color      = Color.objects.get(name = color_name)
        products = color.product_set.values(
            'name', 'main_image', 'sub_image', 'price', 'tag'
        )
        return JsonResponse(
            {'products':list(products)},
            status = 200
        )