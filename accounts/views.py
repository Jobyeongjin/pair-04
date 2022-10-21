
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm

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

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'accounts:index')
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html",
    {
        'form': form, 
    })

