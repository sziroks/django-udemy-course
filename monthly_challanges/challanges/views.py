from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .consts import MONTHLY_CHALLANGES

# Create your views here.


def monthly_challange_number(request, month):
    months = list(MONTHLY_CHALLANGES.keys())
    if month > len(months):
        raise Http404()

    redirected_month = months[month - 1]
    redirect_path = reverse("month-challange", args=[redirected_month])

    return HttpResponseRedirect(redirect_path)


def monthly_challange(request, month):
    try:
        challange_text = MONTHLY_CHALLANGES[month]
        return render(
            request,
            "challanges/challange.html",
            {"challange": challange_text, "month": month},
        )
    except Exception:
        raise Http404()


def index(request):
    months = list(MONTHLY_CHALLANGES.keys())
    return render(request, "challanges/index.html", {"months": months})
