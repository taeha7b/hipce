import json

from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

from .models          import Category, Product, Color

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
        '''만든 이: 이태현
        최종 수정: 2020. 08. 26.
        정보: Shop 페이지 카테고리 별 상품 이름 및 이미지 정보를 보내주는 GET방식 함수
        설명
        - 카테고리를 기준으로 필터해주기 위해 get을 통한 쿼리 스트링 사용
        - 여러 컬러를 필터해주기 위해 getlist을 통한 쿼리 스트링 사용
        - 카테고리의 값에 아무 것도 들어가지 않았을 경우(Default) lip 카테고리 상품을 보여줌
        - 컬러의 값에 아무 것도 들어가지 않았을 경우(Default) 모든 제품을 보여주기 위해 if를 사용
          color_list에 값이 들어간 경우 그 값을 가진 상품 정보들만 필터
        - 프론트 엔드에 정보만 전달하면 되고 키, 밸류로 값을 사용하기 때문에 values 쿼리셋 사용'''
        category_name = request.GET.get('category', 'lip')
        color_list    = request.GET.getlist('color', None)
        products      = Product.objects.prefetch_related('color').filter(
            category__name = category_name
        )
        if color_list:
            products = products.filter(color__name__in = color_list)
        products = products.values('name', 'main_image', 'sub_image', 'price', 'tag')
        return JsonResponse(
            {'products':list(products)},
            status = 200
        )

class ProductView(View):
    def get(self, request, id):
        '''만든 이: 이태현
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

class ColorsView(View):
    def get(self, request):
        '''만든 이: 이태현
        최종 수정: 2020. 08. 25.
        정보: Shop 페이지 컬러 리스트를 보여주는 GET방식 함수
        설명
        - 프론트 엔드에 정보만 전달하면 되고 키, 밸류로 값을 사용하기 때문에 values 쿼리셋 사용'''
        colors = Color.objects.values('name')
        return JsonResponse(
            {'colors':list(colors)},
            status = 200
        )
