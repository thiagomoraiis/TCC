from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'sector', 'telephone', 'coordinator',
        'email', 'posted_by'
    ]
