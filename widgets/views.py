from .models import Bookmark
from django.views.generic import ListView


class BookmarkListView(ListView):
    model = Bookmark
