from .models import Post
from django.views.generic import ListView, DetailView

class PublishedPostMixin(object):
    def get_queryset(self):
        queryset = super(PublishedPostMixin).get_queryset()
        return quesryset.filter(published=True)


class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post
