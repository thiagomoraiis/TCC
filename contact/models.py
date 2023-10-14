from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    sector = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    coordinator = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    posted_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self) -> str:
        return self.sector
