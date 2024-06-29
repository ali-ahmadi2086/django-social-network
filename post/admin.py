from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'slug', 'updated']
    search_fields = ['body', 'slug']
    raw_id_fields = ['user']
    list_filter = ['updated']
    prepopulated_fields = {'slug': ['body']}
    
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'created', 'is_replay']
    raw_id_fields = ['user', 'post', 'reply']

    
