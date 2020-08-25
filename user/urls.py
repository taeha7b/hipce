from django.urls import path

from .views import (
    SignUp, 
    SignIn,
    DeliveryAddress,
)

urlpatterns = [
    path('/signup', SignUp.as_view()),
    path('/signin', SignIn.as_view()),
    path('/delivery_address', DeliveryAddress.as_view()),
]