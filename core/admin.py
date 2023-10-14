from django.contrib import admin # noqa
from .models import PostCategory


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]
