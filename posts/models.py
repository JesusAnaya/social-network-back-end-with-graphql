from django.db import models
from thumbnails.fields import ImageField


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = ImageField()
    description = models.TextField(default='')
