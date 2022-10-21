from django.shortcuts import render, redirect

from reviews.models import Review, Comment
from .forms import ReviewForm, CommentForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'reviews/index.html')

def create(request):
    user = request.user
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = user
            review.save()
            return redirect('review:index')
    else:
        form = ReviewForm()
    return render(request, 'reviews/create.html',
    {
        'form': form,
    })

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

