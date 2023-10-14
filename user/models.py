from django.db import models
from django.contrib.auth.models import User
from city.models import City


class Profile(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    age = models.IntegerField()
    is_student = models.BooleanField(default=True)
    city = models.ForeignKey(
        City, on_delete=models.CASCADE
    )
    bio = models.TextField()
    photo = models.ImageField()

    def __str__(self):
        return self.user
