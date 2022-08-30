from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PlatformUser(models.Model):
    username = models.CharField(max_length = 15)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 30)
    profile_picture = models.ImageField(upload_to = 'profile_pictures/', null = True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.username

class Course(models.Model):
    id = models.IntegerField(primary_key = True)
    title = models.CharField(max_length = 30)
    short_description = models.TextField()
    long_description = models.TextField()
    image = models.ImageField(upload_to = 'courses_icons/', null = False, blank = False)

    def __str__(self):
        return self.title

