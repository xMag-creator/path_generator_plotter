# Generated by Django 3.2.7 on 2021-09-22 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='height',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='image',
            name='width',
            field=models.IntegerField(default=100),
        ),
    ]
