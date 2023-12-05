from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class PostCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    CATEGORY_CHOICES = (
        ('dicas', 'Dicas'),
        ('eventos', 'Eventos')
    )
    title = models.CharField(
        max_length=200
    )
    description = models.TextField()
    content = RichTextUploadingField()
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES
    )
    posted_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    posted_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.title
