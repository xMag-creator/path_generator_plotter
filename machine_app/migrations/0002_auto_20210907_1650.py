# Generated by Django 3.2.7 on 2021-09-07 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machine_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='u_min_range',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='machine',
            name='v_min_range',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='machine',
            name='w_min_range',
            field=models.FloatField(default=0.0),
        ),
    ]
