from django.db import models
from django.db.models.fields.files import ImageFieldFile


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=200)
    description = models.TextField()
    image_pokemon = models.ImageField(upload_to='image', blank=True)
    published = models.BooleanField(default=False)