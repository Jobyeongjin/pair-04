from unittest import mock
from django.shortcuts import render, redirect
from reviews.models import Review, Comment
from movies.models import Movie
from .forms import ReviewForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.db.models import Q

def index(request, movie_pk):
    movie = Movie.objects.get(pk = movie_pk)
    reviews = movie.review_set.all()
    return render(
        request,
        "reviews/index.html",
        {
            "reviews": reviews,
            "movie" : movie,
        },
    )

@login_required
def create(request, movie_pk):
    movie = Movie.objects.get(pk = movie_pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
            return redirect("review:index", movie_pk)
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
def update(request, movie_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, request.FILES, instance=review)
            if form.is_valid():
                form.save()
                return redirect('review:detail', movie_pk, review.pk)
        else:
            form = ReviewForm(instance=review)
        return render(request, 'reviews/update.html',
        {
            'form': form,
        })
    else:
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden()

@login_required
def delete(request, movie_pk, review_pk):
    review = Review.objects.get(pk = review_pk)
    if request.user == review.user:
        review.delete()
    else:
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden()
    return redirect('review:index', movie_pk)


def detail(request, review_pk, movie_pk):
    movie = Movie.objects.get(pk = movie_pk)
    # review = Review.objects.filter(pk = review_pk)
    review = Review.objects.get(pk = review_pk)
    
    comment_form = CommentForm()
    context = {
        'review' : review,
        'comments' : review.comment_set.filter(movie=movie_pk),
        # 'comments' : review.comment_set.all(),
        'comment_form' : comment_form,
    }
    print(type(review.comment_set.all()), review.comment_set.all())
    return render(request, 'reviews/detail.html', context )

def create_comment(request, movie_pk ,review_pk):
    movie = Movie.objects.get(pk = movie_pk)
    review = Review.objects.get(pk = review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.movie = movie
        comment.user = request.user
        comment.save()
    return redirect('review:detail', movie_pk ,review.pk)

def delete_comment(request, movie_pk, review_pk, comment_pk):
    movie = Movie.objects.get(pk = movie_pk)
    comment = Comment.objects.get(pk = comment_pk)
    review = Review.objects.get(pk = review_pk)
    if request.user == review.user:
        comment.delete()
    return redirect('review:detail', movie_pk, review.pk)

from django.views.generic import FormView
from .forms import ReviewSearchForm
# model orm으로 where 절에 or문을 추가하고 싶을 때 사용.
# https://velog.io/@mongle/Django-Web-Project-%EA%B0%9C%EB%B0%9C%EC%9D%BC%EC%A7%804-%EA%B2%80%EC%83%89-%EA%B8%B0%EB%8A%A5-%EC%B6%94%EA%B0%80

from django.urls import reverse

class SearchFormView(FormView):
    form_class = ReviewSearchForm
    template_name = 'reviews/review_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        review_list = Review.objects.filter(Q(movie_name__icontains=searchWord) | Q(title__icontains=searchWord) | Q(content__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = review_list

        return render(self.request, self.template_name, context)
@require_POST
def likes(request, movie_pk ,review_pk):
    movie = Movie.objects.get(pk = movie_pk)
    if request.user.is_authenticated:
        review = Review.objects.get(pk = review_pk)

        if review.like_users.filter(pk=request.user.pk).exists():
            review.like_users.remove(request.user)

        else:
            review.like_users.add(request.user)
        return redirect('review:detail', movie.pk, review_pk)
    return redirect('accounts:login')


