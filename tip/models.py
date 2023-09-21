from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Dica(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    postado_em = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True
    )
    postado_por = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self) -> str:
        return self.titulo