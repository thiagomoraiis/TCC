from django.contrib import admin
from .models import Tip


@admin.register(Tip)
class TipAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'posted_at', 'posted_by'
    ]
