from .models import Biodata, Project
from django.views.generic import ListView

class BiodataListView(ListView):
    model = Biodata

class ProjectListView(ListView):
    model = Project
