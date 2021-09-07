# Generated by Django 3.2.7 on 2021-09-07 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('x_max_range', models.FloatField(default=100.0)),
                ('y_max_range', models.FloatField(default=100.0)),
                ('z_max_range', models.FloatField(default=100.0)),
                ('u_max_range', models.FloatField(default=0.0)),
                ('v_max_range', models.FloatField(default=0.0)),
                ('w_max_range', models.FloatField(default=0.0)),
                ('z_push_pos', models.FloatField(default=0.0)),
                ('z_jump_lim', models.FloatField(default=10.0)),
                ('x_sheet_offset', models.FloatField(default=0.0)),
                ('y_sheet_offset', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('diameter', models.FloatField()),
            ],
        ),
    ]
