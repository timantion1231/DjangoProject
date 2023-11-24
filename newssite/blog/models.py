from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# User =get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=255)
    #author = models.ForeignKey('user', on_delete= models.CASCADE)
    content = models.TextField()
    is_published = models.BooleanField(default= True)

   # class PostStatus

    def __str__(self):
        return self.title