from django.contrib import admin
from .models import Post, Tweet

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    fields = ('title','slug','description','content','published','enable_comments','author')
    list_display = ['published','title', 'author', 'updated_at']
    list_display_links = ['title']
    list_editable = ['published']
    list_filter = ['published', 'author']
    prepopulated_fields = {'slug': ['title',]}
    search_fields = ['title','content']

class TweetAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Tweet, TweetAdmin)

