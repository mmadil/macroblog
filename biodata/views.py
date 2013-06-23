from .models import Biodata
from django.views.generic import ListView

class BiodataListView(ListView):
    model = Biodata
