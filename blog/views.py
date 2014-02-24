from .models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView

class PostListView(ListView):
    model = Post
    queryset = Post.public_post.all()

class PostDetailView(DetailView):
    model = Post

