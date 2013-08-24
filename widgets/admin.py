from django.contrib import admin
from .models import Quote, Bookmark

class QuoteAdmin(admin.ModelAdmin):
    fields = ('quotation', 'quoted_by')
    list_display = ['use_it', 'quotation', 'quoted_by']
    list_display_links = ['quotation']
    list_editable = ['use_it']
    list_filter = ['quoted_by']
    search_fields = ['quoted_by', 'quotation']

class BookmarkAdmin(admin.ModelAdmin):
    fields = ('title', 'link', 'description')
    list_display = ['show', 'title', 'link','updated_at']
    list_display_links = ['title']
    list_editable = ['show']
    list_filter = ['show']
    search_fields = ['title']

admin.site.register(Quote, QuoteAdmin)
admin.site.register(Bookmark, BookmarkAdmin)
