from django.contrib import admin
from .models import Tip, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]


@admin.register(Tip)
class TipAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'posted_in', 'posted_by'
    ]
