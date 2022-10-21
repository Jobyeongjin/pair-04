from django.shortcuts import render, redirect
from .forms import ReviewForm


def index(request):
    return render(request, 'reviews/index.html')

def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review:index')
    else:
        form = ReviewForm()
    return render(request, 'reviews/create.html',
    {
        'form': form,
    })
