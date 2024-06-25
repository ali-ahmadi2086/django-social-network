from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'slug', 'updated']
    search_fields = ['body', 'slug']
    raw_id_fields = ['user']