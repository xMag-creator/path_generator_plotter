from django.db import models
from django.contrib.auth.models import User
from image_app.models import Image
from machine_app.models import Machine
from project_app.models import Project, Tool


# Create your models here.
class Resources(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    projects = models.ForeignKey(Project, on_delete=models.CASCADE)
    images = models.ForeignKey(Image, on_delete=models.CASCADE)
    tools = models.ForeignKey(Tool, on_delete=models.CASCADE)
    machines = models.ForeignKey(Machine, on_delete=models.CASCADE)
