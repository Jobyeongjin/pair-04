from django.shortcuts import render, redirect
from reviews.models import Review, Comment
from .forms import ReviewForm, CommentForm
from django.contrib.auth.decorators import login_required

def index(request):
    reviews = Review.objects.order_by("-pk")
    return render(
        request,
        "reviews/index.html",
        {
            "reviews": reviews,
        },
    )

@login_required
def create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
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

@login_required
def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.user == review.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, request.FILES, instance=review)
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

@login_required
def delete(request, pk):
    review = Review.objects.get(pk=pk)
    if request.user == review.user:
        review.delete()
    else:
        return HttpResponseForbidden()
    return redirect('review:index')


def detail(request, review_pk):
    return render(request, 'reviews/detail.html', )

def create_comment(request, review_pk):
    review = Review.objects.get(pk = review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
    return redirect('reviews:index')

def delete_comment(request, review_pk, comment_pk):
    comment = Comment.objects.get(pk = comment_pk)
    review = Review.objects.get(pk = review_pk)
    if request.user == review.user:
        comment.delete()
    return redirect('reviews:index')

