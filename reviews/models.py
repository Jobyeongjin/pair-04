from django.db import models
from django.conf import settings


class Review(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    movie_name = models.CharField(max_length=30)
    grade = models.IntegerField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
