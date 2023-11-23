from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 50
