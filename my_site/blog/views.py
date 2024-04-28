from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from datetime import date
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Post


def get_date(post):
    return post["date"]


class StartingPageView(View):
    def get(self, request):
        latest_posts = Post.objects.order_by("-date")[:3]
        return render(request, "blog/index.html", {"posts": latest_posts})
    
class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = "all_posts"

class PostDetailView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post
    