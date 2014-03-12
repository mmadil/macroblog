from .models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView

class PostListView(ListView):
    model = Post
    queryset = Post.public_post.filter(status__gte=2)

class PostDetailView(DetailView):
    model = Post

