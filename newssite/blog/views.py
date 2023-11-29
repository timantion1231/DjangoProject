from django.http import HttpResponse
from django.views.generic import ListView, DeleteView, UpdateView, DetailView
from django.views.generic.edit import CreateView
from .models import Post
from  django.urls import reverse_lazy



class BlogListView(ListView):
    model = Post
    paginate_by = 50


class BlogDetailView(DeleteView):
    model = Post
    template_name = 'blog/post_detail.html'


class BlogCreatePost(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = ['title', 'content', 'self.request']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'content']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')