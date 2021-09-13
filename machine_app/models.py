from django.db import models


# Create your models here.
class Tool(models.Model):
    name = models.CharField(max_length=64)
    diameter = models.FloatField()


class Machine(models.Model):
    # model to describe machine (plotter) parameters
    name = models.CharField(max_length=64)
    # if max_range > 0 -> axis exist
    x_max_range = models.FloatField(default=100.0)
    y_max_range = models.FloatField(default=100.0)
    z_max_range = models.FloatField(default=100.0)
    u_max_range = models.FloatField(default=0.0)
    u_min_range = models.FloatField(default=0.0)
    v_max_range = models.FloatField(default=0.0)
    v_min_range = models.FloatField(default=0.0)
    w_max_range = models.FloatField(default=0.0)
    w_min_range = models.FloatField(default=0.0)
    z_push_pos = models.FloatField(default=0.0)
    z_jump_lim = models.FloatField(default=10.0)
    x_sheet_offset = models.FloatField(default=0.0)
    y_sheet_offset = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

