from django.db import models


# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=64)
    path = models.ImageField(upload_to='images/')

    def delete(self, using=None, keep_parents=False):
        self.path.storage.delete(self.path.name)
        super(Image, self).delete()
