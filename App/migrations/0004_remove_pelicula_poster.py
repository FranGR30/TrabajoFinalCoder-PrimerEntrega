# Generated by Django 4.0.4 on 2022-05-11 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_alter_pelicula_poster'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelicula',
            name='poster',
        ),
    ]
