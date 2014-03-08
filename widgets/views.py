from .models import Bookmark
from django.views.generic import ListView
from django.shortcuts import render

def GalleryHome(request):
    return render(request, 'gallery.html',{})

class BookmarkListView(ListView):
    model = Bookmark
