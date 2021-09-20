from django.db import models
from image_app.models import Image
from machine_app.models import Machine, Tool
from path_generator import convert_image_to_path


# Create your models here.
class Project(models.Model):
    # model describing projects
    name = models.CharField(max_length=64)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    sheet_width = models.FloatField(default=210)
    sheet_height = models.FloatField(default=297)
    image_position_x = models.FloatField(default=0)
    image_position_y = models.FloatField(default=0)
    image_size = models.FloatField(default=100)
    image_rotation = models.FloatField(default=0)
    resolution = models.FloatField(default=0)
    g_code = models.TextField(default='')

    def __str__(self):
        return self.name

    def generate_g_code(self):
        return convert_image_to_path(self.image.path, self.image_size)
