from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.main, name='main'),
    path('accounts/signup/', views.signup, name='signup'),
    path("accounts/login/", views.login, name="login"),
    path("accounts/logout/", views.logout, name="logout"),
    path("accounts/profile/<int:user_pk>", views.profile, name="profile"),
    path("accounts/update/<int:user_pk>", views.update, name="update"),
    path("accounts/delete/", views.delete, name="delete"),
    path("accounts/password/<int:user_pk>", views.change_password, name="change_password"),   
    path("accounts/create_profile/<int:user_pk>", views.create_profile, name="create_profile"),
    path("accounts/update_profile/<int:profile_pk>", views.update_profile, name="update_profile"), 
]
