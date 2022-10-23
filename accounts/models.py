from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import os
# Create your models here.
class User(AbstractUser):
    pass

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='accounts/dafault.png', upload_to='accounts/', blank = True, null = True)
    bio = models.TextField()
    background_image = models.ImageField(default='accounts/background/dafault.png', upload_to='accounts/background/', blank = True, null = True)
    def delete(self, *args, **kargs):
        if self.upload_files:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.upload_files.path))
        super(Profile, self).delete(*args, **kargs)
