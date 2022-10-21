from django.db import models

# Create your models here.

class Movie(models.Model):
    id = models.IntegerField(primary_key = True)
    title = models.CharField(max_length = 80)
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.URLField()