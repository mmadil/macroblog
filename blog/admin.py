from django.contrib import admin
from .models import Post, Like

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    prepopulated_fields = {'slug': ['title',]}
    search_fields = ['title','content']

class LikeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Like, LikeAdmin)

