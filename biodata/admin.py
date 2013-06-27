from django.contrib import admin
from .models import Biodata, Project

class BiodataAdmin(admin.ModelAdmin):
    fields = ('heading', 'order', 'content', 'published')
    list_display = ['published', 'order', 'heading']
    list_display_links = ['heading']
    list_editable = ['published', 'order']
    list_filter = ['published']
    search_fields = ['heading', 'content']

class ProjectAdmin(admin.ModelAdmin):
    fields = ('heading', 'content', 'published')
    list_display = ['published', 'heading']
    list_display_links = ['heading']
    list_editable = ['published']
    list_filter = ['published']
    search_fields = ['heading', 'content']

admin.site.register(Biodata, BiodataAdmin)
admin.site.register(Project, ProjectAdmin)
