from typing import Any
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from datetime import date
from django.views import View
from django.views.generic import ListView, DetailView
from django.urls import reverse

from .models import Post
from .forms import CommentForm


class StartingPageView(View):
    def get(self, request):
        latest_posts = Post.objects.order_by("-date")[:3]
        return render(request, "blog/index.html", {"posts": latest_posts})


class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = "all_posts"


class PostDetailView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        id_post = post.id_post
        read_later = str(id_post) == request.session.get("read_later")
        context = self.get_context(
            post,
            CommentForm(),
            read_later,
        )
        return render(
            request,
            "blog/post-detail.html",
            context=context,
        )

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.id_post = post
            comment.save()
            return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        id_post = post.id_post
        read_later = str(id_post) == request.session.get("read_later")
        context = self.get_context(
            post,
            comment_form,
            read_later,
        )
        return render(
            request,
            "blog/post-detail.html",
            context=context,
        )

    @staticmethod
    def get_context(post, comment_form, read_later):
        context = {
            "post": post,
            "comment_form": comment_form,
            "read_later": read_later,
            "comments": post.comments.all().order_by("-id_comment"),
        }
        return context


class ReadLaterView(View):
    def post(self, request):
        post_id = request.POST.get("id_post")
        post = Post.objects.get(pk=post_id)
        request.session["read_later"] = post_id
        slug = post.slug
        return HttpResponseRedirect("/blog/posts/" + slug)
