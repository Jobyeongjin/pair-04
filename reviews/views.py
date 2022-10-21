from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
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


def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.user == review.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                return redirect('review:detail', review.pk)
        else:
            form = ReviewForm(instance=review)
        return render(request, 'reviews/update.html',
        {
            'form': form,
        })
    else:
        return HttpResponseForbidden()