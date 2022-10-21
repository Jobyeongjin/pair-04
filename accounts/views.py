
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

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

def profile(request, user_pk):
    user = get_user_model().objects.get(pk = user_pk)
    context = {
        "user" : user
    }
    return render(request, 'accounts/profile.html', context)

def update(request, user_pk):
    update_form = CustomUserChangeForm(instance=request.user)
    if request.method == "POST":
        update_form = CustomUserChangeForm(request.POST, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            return redirect('accounts:profile', user_pk)
    context = {
        "update_form" : update_form,
    }
    return render(request, 'accounts/update.html', context)

def change_password(request, user_pk):
    user = get_user_model().objects.get(pk = user_pk)
    password_form = PasswordChangeForm(request.user)
    if request.method == "POST":
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            password_form.save()
            return redirect('accounts:profile', user.pk)
    context = {
        'password_form' : password_form,
    }
    return render(request, 'accounts/change_password.html', context)
