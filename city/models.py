from django.db import models
from django.contrib.auth.models import User


class Cidade(models.Model):
    nome = models.CharField(max_length=200)
    onibus_dispo = models.BooleanField(default=True)
    postado_por = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self) -> str:
        return self.nome
