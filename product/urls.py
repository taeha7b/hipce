from django.urls import path

from .views      import CategoryView, ProductsView, ProductView, ColorsView, CollectionsView

urlpatterns = [
    path('/category', CategoryView.as_view()),
    path('', ProductsView.as_view()),
    path('/<int:product_id>', ProductView.as_view()),
    path('/colors', ColorsView.as_view()),
    path('/collections', CollectionsView.as_view()),
]