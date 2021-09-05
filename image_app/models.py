from django.db import models


# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=64)
    path = models.ImageField(upload_to='images/')
