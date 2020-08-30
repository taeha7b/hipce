from django.urls import path, include

urlpatterns = [
    path('users', include('user.urls')),
    path('reviews', include('reviews.urls')),
    path('products', include('product.urls')),
    path('orders', include('order.urls')),
]
