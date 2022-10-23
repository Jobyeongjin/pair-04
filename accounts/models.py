from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.
class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='dafault.png', upload_to='accounts/', blank = True)
    bio = models.TextField()
    
