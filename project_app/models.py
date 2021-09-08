from django.db import models
from image_app.models import Image
from machine_app.models import Machine


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=64)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
