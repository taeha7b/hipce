from django.urls import path

from .views      import CategoryView, ProductsView, ProductView, ColorsView

urlpatterns = [
    path('', CategoryView.as_view()),
    path('/products', ProductsView.as_view()),
    path('/products/<int:id>', ProductView.as_view()),
    path('/colors', ColorsView.as_view()),
]