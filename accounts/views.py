
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

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
            user = signup_form.save()
            auth_login(request, user)
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
@login_required
def logout(request):
    auth_logout(request)
    return redirect('accounts:index')

@login_required
def profile(request, user_pk):
    user = get_user_model().objects.get(pk = user_pk)
    context = {
        "user" : user
    }
    return render(request, 'accounts/profile.html', context)

@login_required
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

@login_required
def change_password(request, user_pk):
    user = get_user_model().objects.get(pk = user_pk)
    password_form = PasswordChangeForm(request.user)
    if request.method == "POST":
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            password_form.save()
            update_session_auth_hash(request, password_form.user)
            return redirect('accounts:profile', user.pk)
    context = {
        'password_form' : password_form,
    }
    return render(request, 'accounts/change_password.html', context)

@login_required
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('accounts:index')