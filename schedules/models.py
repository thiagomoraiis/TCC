from django.db import models
from django.contrib.auth.models import User
from city.models import Cidade


class RotaOnibus(models.Model):
    TURNO_CHOICES = (
        ('matutino', 'Matutino'),
        ('vespertino', 'Vespertino'),
        ('noturno', 'Noturno')
    )
    origem = models.ForeignKey(
        Cidade, on_delete=models.CASCADE
    )
    destino = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    turno = models.CharField(
        choices=TURNO_CHOICES, max_length=12
    )
    horario_chegada = models.CharField(max_length=100)
    horario_saida = models.CharField(max_length=100)
    postado_por = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self) -> str:
        return self.origem + ' - ' + self.destino
