from django.db import models
from django.contrib.auth.models import User


class HorarioOnibus(models.Model):
    TURNO_CHOICES = (
        ('matutino', 'Matutino'), ('vespertino', 'Vespertino'),
        ('noturno', 'Noturno')
    )
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    turno = models.CharField(choices=TURNO_CHOICES, max_length=12)
    horario_chegada = models.CharField(max_length=100)
    horario_saida = models.CharField(max_length=100)
    postado_por = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
