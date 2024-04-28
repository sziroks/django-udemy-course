from typing import Any
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from datetime import date
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Post


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

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        selected_post = self.object.id_post
        request = self.request
        rl_post = request.session.get("read_later")
        context["read_later"] = str(selected_post) == rl_post
        print(str(selected_post), rl_post)

        return context

class ReadLaterView(View):
    def post(self, request):
        post_id = request.POST.get("id_post")
        post = Post.objects.get(pk=post_id)
        request.session["read_later"] = post_id
        slug = post.slug
        return HttpResponseRedirect("/blog/posts/" + slug)