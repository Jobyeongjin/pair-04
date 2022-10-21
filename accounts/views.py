from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
# Create your views here.
def index(request):
    users = get_user_model().objects.all()
    context = {
        "users": users
    }

    return render(request, 'accounts/index.html', context)

def signup(request):
    signup_form = CustomUserCreationForm()
    if request.method == "POST":
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return redirect('accounts:index')

    context = {
        "signup_form" : signup_form,
    }
    return render(request, 'accounts/signup.html', context)