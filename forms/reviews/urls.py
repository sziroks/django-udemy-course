from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view(), name="review"),
    path("thank-you", views.thank_your, name="thank-you"),
]
