from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse


# User =get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=255)
    # author = models.ForeignKey('user', on_delete= models.CASCADE)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
