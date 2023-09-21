from django.contrib import admin
from .models import Dica, Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
    ]


@admin.register(Dica)
class DicaAdmin(admin.ModelAdmin):
    list_display = [
        'titulo', 'postado_em', 'postado_por'
    ]
