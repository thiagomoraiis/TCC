from django.db import models
from django.contrib.auth.models import User
from city.models import Cidade


class Perfil(models.Model):
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    idade = models.IntegerField()
    is_estudante = models.BooleanField(default=True)
    cidade = models.ForeignKey(
        Cidade, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.usuario
