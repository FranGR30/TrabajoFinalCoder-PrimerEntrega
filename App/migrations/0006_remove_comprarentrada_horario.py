# Generated by Django 4.0.4 on 2022-05-12 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_comprarentrada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comprarentrada',
            name='horario',
        ),
    ]
