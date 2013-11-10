from .models import Post
from django.views.generic import ListView, DetailView

class PostListView(ListView):
    model = Post
    queryset = Post.published_post.all()

class PostDetailView(DetailView):
    model = Post
