from django.db import models
from core.models import Post


class Event(Post):
    date = models.DateField()
    local = models.TextField()

    def __str__(self) -> str:
        return self.date + ' ' + self.local
