from django.urls import path

from .views import ReviewView, ReviewReplyView

urlpatterns = [
    path('', ReviewView.as_view()),
    path('/<int:id>', ReviewView.as_view()),
    path('/review-reply', ReviewReplyView.as_view()),
    path('/review-reply/<int:id>', ReviewReplyView.as_view()),
]