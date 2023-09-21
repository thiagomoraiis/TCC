from django.db import models
from django.contrib.auth.models import User


class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField()
    local = models.CharField(max_length=150)
    imagem1 = models.ImageField(
        upload_to='eventos/%y/%m/%d'
    )
    imagem2 = models.ImageField(
        upload_to='eventos/%y/%m/%d', default=None
    )
    postado_por = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
