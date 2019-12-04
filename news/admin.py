from django.contrib import admin
from .models import Article, Comment
from django.contrib.auth.decorators import permission_required


admin.site.site_header = "FountainHub Admin"
admin.site.site_title = "FountainHub Admin Portal"
admin.site.index_title = "Welcome to FountainHub News Portal"


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['reporter', 'headline', 'pub_date']
    list_filter = ['reporter', 'pub_date']



class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'article', 'created_date', 'moderation']
    list_filter = ['moderation']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
