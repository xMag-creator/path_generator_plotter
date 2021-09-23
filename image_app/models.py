from django.db import models
from path_generator import load_image


# Create your models here.
class Image(models.Model):
    # model describing image
    name = models.CharField(max_length=64)
    path = models.ImageField(upload_to='images/')
    width = models.IntegerField(default=100)
    height = models.IntegerField(default=100)

    def __str__(self):
        return self.name

    def read_image_size(self):
        return load_image(self.path)[1]

    def delete(self, using=None, keep_parents=False):
        self.path.storage.delete(self.path.name)
        super(Image, self).delete()
