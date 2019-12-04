from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'published_date', 'total_likes', 'category']
    list_filter = ['author', 'published_date', 'category']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_date', 'moderation']
    list_filter = ['moderation']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
