from django.contrib import admin
from .models import Quote

class QuoteAdmin(admin.ModelAdmin):
    fields = ('quotation', 'quoted_by')
    list_display = ['use_it', 'quotation', 'quoted_by']
    list_display_links = ['quotation']
    list_editable = ['use_it']
    list_filter = ['quoted_by']
    search_fields = ['quoted_by', 'quotation']

admin.site.register(Quote, QuoteAdmin)
