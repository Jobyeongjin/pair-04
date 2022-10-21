from django.urls import path
from . import views

app_name = "review"

urlpatterns = [
    path('<int:movie_pk>/', views.index, name='index'),
    path('<int:movie_pk>/create/', views.create, name='create'),
    path('<int:movie_pk>/<int:review_pk>/update/', views.update, name='update'),
    path('<int:movie_pk>/<int:review_pk>/delete/', views.delete, name='delete'),
    path('<int:movie_pk>/<int:review_pk>/detail/', views.detail, name='detail'),
    path('<int:movie_pk>/create_comment/<int:review_pk>', views.create_comment, name='create_comment'),
    path('<int:movie_pk>/<int:review_pk>/comments/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
    path('search/', views.SearchFormView.as_view(), name='search'),
    path('<int:movie_pk>/<int:review_pk>/likes', views.likes, name='likes'),
]
