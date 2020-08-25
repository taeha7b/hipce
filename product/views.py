import json

from django.views import View
from django.http  import JsonResponse

from .models      import Category, Product

class CategoryShowView(View):
    def get(self, request):
        ''' 만든 이: 이태현
        최종 수정: 2020. 08. 25.
        정보: Shop 페이지 카테고리 이름 및 이미지 정보를 보내주는 GET방식 함수
        설명: 프론트 엔드에 정보만 전달하면 되고 키, 밸류로 값을 사용하기 때문에 values 쿼리셋 사용'''
        categories = Category.objects.values('name', 'image')
        return JsonResponse(
            {'category':list(categories)},
            status = 200
        )

class ProductShowview(View):
    def get(self, request):
        ''' 만든 이: 이태현
        최종 수정: 2020. 08. 25.
        정보: Shop 페이지 상품 이름, 이미지들, 가격, 태그 이미지를 보내주는 GET방식 함수
        설명: 프론트 엔드에 정보만 전달하면 되고 키, 밸류로 값을 사용하기 때문에 values 쿼리셋 사용'''
        products = Product.objects.values('name', 'main_image', 'sub_image', 'price', 'tag')
        return JsonResponse(
            {'product':list(products)},
            status = 200
        )
