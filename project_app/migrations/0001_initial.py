# Generated by Django 3.2.7 on 2021-09-19 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('image_app', '0001_initial'),
        ('machine_app', '0003_tool_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('sheet_width', models.FloatField(default=210)),
                ('sheet_height', models.FloatField(default=297)),
                ('image_position_x', models.FloatField(default=0)),
                ('image_position_y', models.FloatField(default=0)),
                ('image_size', models.FloatField(default=100)),
                ('image_rotation', models.FloatField(default=0)),
                ('resolution', models.FloatField(default=0)),
                ('g_code', models.TextField(default='')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='image_app.image')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machine_app.machine')),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='machine_app.tool')),
            ],
        ),
    ]
