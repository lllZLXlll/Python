from django.contrib import admin

"""
后台账户
"""

from django.contrib import admin
from .models import Post, Category, Tag, News

class PostAdmin (admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author', 'views']

class NewsAdmin (admin.ModelAdmin):
    list_display = ['title', 'url', 'created_time']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(News, NewsAdmin)