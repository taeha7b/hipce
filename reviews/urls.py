from django.urls import path

from .views import Review

urlpatterns = [
    path('', Review.as_view())
]