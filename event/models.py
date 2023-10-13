from django.db import models
from django.contrib.auth.models import User


class Evento(models.Model):
    titulo = models.CharField(max_length=150)
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField()
    conteudo = models.TextField()
    local = models.CharField(max_length=150)
    postado_por = models.ForeignKey(User, on_delete=models.CASCADE)
