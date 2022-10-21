from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review


def index(request):
    reviews = Review.objects.order_by("-pk")
    return render(
        request,
        "reviews/index.html",
        {
            "reviews": reviews,
        },
    )


def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect("review:index")
    else:
        form = ReviewForm()
    return render(
        request,
        "reviews/create.html",
        {
            "form": form,
        },
    )
