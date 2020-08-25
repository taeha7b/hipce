from django.urls import path

from .views import CategoryShowView, ProductShowview

urlpatterns = [
    path('', CategoryShowView.as_view()),
    path('/product', ProductShowview.as_view())
]