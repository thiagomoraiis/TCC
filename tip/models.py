from django.db import models
from core.models import Post


class Tip(Post):
    TIP_ABOUT_CHOICES = (
        ('option 1', 'Option 1'),
        ('option 2', 'Option 2'),
        ('option 3', 'Option 3'),
    )
    tip_about = models.CharField(
        max_length=20, choices=TIP_ABOUT_CHOICES
    )

    def __str__(self) -> str:
        return self.tip_about
