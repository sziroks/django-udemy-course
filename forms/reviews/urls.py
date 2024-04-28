from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewSubmitView.as_view(), name="review-form"),
    path("thank-you", views.ThankYouView.as_view(), name="thank-you"),
    path("reviews", views.ReviewView.as_view(), name="reviews"),
    path("reviews/favorite", views.AddFavoriteView.as_view()),
    path("reviews/<int:pk>", views.ReviewDetailView.as_view(), name="review-detail"),
]
