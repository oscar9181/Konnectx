from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name_artist = models.CharField(max_length=255, blank=True,null=True)
    role_artist = models.CharField(max_length=255, blank=True, null=True)
    profile_image = models.ImageField(upload_to ='images/',default= 'default-img.jpg')
    location = models.CharField(max_length=25, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    website = models.URLField(max_length=250)
         