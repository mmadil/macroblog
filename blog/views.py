from .models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView

def ThoughtsView(request):
    recents_post = Post.published_post.all().order_by('-updated_at')[:5]
    # TODO
    # Fetch recent tweets from Twitter.
    return render(request, 'thoughts.html', {})

class PostListView(ListView):
    model = Post
    queryset = Post.published_post.all()

class PostDetailView(DetailView):
    model = Post
