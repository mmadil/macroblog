from django.contrib import admin

from .models import Picture, Category

class PictureAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Picture, PictureAdmin)
admin.site.register(Category, CategoryAdmin)

