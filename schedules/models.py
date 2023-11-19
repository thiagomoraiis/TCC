from django.db import models
from django.contrib.auth.models import User
from city.models import City


class BusRoute(models.Model):
    SHIFTS_CHOICES = (
        ('matutino', 'Matutino'),
        ('vespertino', 'Vespertino'),
        ('noturno', 'Noturno')
    )
    origin = models.ForeignKey(
        City, on_delete=models.CASCADE
    )
    destiny = models.CharField(
        max_length=16, default='Pau dos Ferros'
    )
    shift = models.CharField(
        choices=SHIFTS_CHOICES, max_length=12
    )
    arrival_time = models.CharField(max_length=100)
    departure_time = models.CharField(max_length=100)
    posted_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.origin + ' - ' + self.destiny
