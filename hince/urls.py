from django.urls import path, include

urlpatterns = [
    path('users', include('user.urls')),
    path('products', include('product.urls')),
    path('shoppingbag', include('order.urls')),
]