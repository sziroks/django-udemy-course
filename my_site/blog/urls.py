from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts/", views.AllPostsView.as_view(), name="posts-page"),
    path("posts/read-later", views.ReadLaterView.as_view()),
    path("posts/<slug:slug>", views.PostDetailView.as_view(), name="post-detail-page"),
]
