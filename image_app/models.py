from django.db import models


# Create your models here.
class Image(models.Model):
    # model describing image
    name = models.CharField(max_length=64)
    path = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.path.storage.delete(self.path.name)
        super(Image, self).delete()
