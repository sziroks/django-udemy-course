from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .forms import ReviewForm
from .models import Review


class ReviewSubmitView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"


class ReviewView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"


class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        fav_id = request.session.get("favorite_review")
        context["is_favorite"] = fav_id == str(loaded_review.id)
        return context


class AddFavoriteView(View):
    def get(self, request):
        pass

    def post(self, request):
        review_id = request.POST.get("review_id")
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)
