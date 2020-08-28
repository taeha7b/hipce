from django.urls import path, include

urlpatterns = [
    path('user', include('user.urls')),
    path('reviews', include('reviews.urls')),
    path('users', include('user.urls')),
    path('products', include('product.urls')),
    path('shoppingbag', include('order.urls')),
]