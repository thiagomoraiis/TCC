from django.contrib import admin
from .models import Contato


@admin.register(Contato)
class ContadoAdmin(admin.ModelAdmin):
    list_display = [
        'setor', 'telefone', 'coordenador',
        'email', 'postado_por'
    ]
