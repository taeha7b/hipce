from django.urls import path

from .views import Review, ReviewReputation, ReviewReply

urlpatterns = [
    path('', Review.as_view()),
    path('review-reputations', ReviewReputation.as_view()),
    path('review-replies', ReviewReply.as_view()),
]