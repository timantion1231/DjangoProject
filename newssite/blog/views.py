from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DeleteView
from .models import Post


class BlogListView(ListView):
    model = Post
    paginate_by = 50

class BlogDetailView(DeleteView):
    model = Post