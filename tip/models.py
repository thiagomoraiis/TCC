from django.db import models
from core.models import Post


class Tip(Post):
    TIP_ABOUT_CHOICES = (
        ('desempenho', 'Desempenho'),
        ('ira', 'IRA'),
        ('bolsas', 'Bolsas'),
        ('cursos', 'Cursos'),
    )
    tip_about = models.CharField(
        max_length=20, choices=TIP_ABOUT_CHOICES
    )

    def __str__(self) -> str:
        return self.tip_about
