from django.contrib import admin
from .models import Cidade


@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'onibus_dispo', 'postado_por')
