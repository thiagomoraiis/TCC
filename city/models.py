from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=200)
    bus_dispo = models.BooleanField(default=True)
    posted_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self) -> str:
        return self.name
