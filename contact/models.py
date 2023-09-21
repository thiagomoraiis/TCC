from django.db import models
from django.contrib.auth.models import User


class Contato(models.Model):
    setor = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    coordenador = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    postado_por = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self) -> str:
        return self.setor
