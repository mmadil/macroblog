from django.contrib import admin
from .models import Quote, Bookmark, Category

class QuoteAdmin(admin.ModelAdmin):
    fields = ('quotation', 'quoted_by')
    list_display = ['use_it', 'quotation', 'quoted_by']
    list_display_links = ['quotation']
    list_editable = ['use_it']
    list_filter = ['quoted_by']
    search_fields = ['quoted_by', 'quotation']

class BookmarkAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Quote, QuoteAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Bookmark, BookmarkAdmin)
