from django.contrib import admin
from .models import Biodata

class BiodataAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    fields = ('heading', 'order', 'content', 'published')
    list_display = ['published', 'order', 'heading']
    list_display_links = ['heading']
    list_editable = ['published', 'order']
    list_filter = ['published']
    search_fields = ['heading', 'content']

admin.site.register(Biodata, BiodataAdmin)
