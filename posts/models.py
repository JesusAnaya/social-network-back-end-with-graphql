from django.db import models
from thumbnails.fields import ImageField


class Post(models.Model):
    title = models.CharField(max_length=255)
    image = ImageField(upload_to='posts')
    description = models.TextField(default='')

    def __str__(self):
        return self.title
