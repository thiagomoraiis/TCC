from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    content = models.TextField()
    local = models.CharField(max_length=150)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
