from django.contrib import admin
from .models import Post 

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    fields = ('title','slug','content','published','enable_comments','author')
    list_display = ['published','title', 'author', 'updated_at']
    list_display_links = ['title']
    list_editable = ['published']
    list_filter = ['published', 'author']
    prepopulated_fields = {'slug': ['title',]}
    search_fields = ['title','content']

admin.site.register(Post, PostAdmin)

