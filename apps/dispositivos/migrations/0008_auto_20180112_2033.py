# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-12 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivos', '0007_auto_20180112_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='fecha_instalacion',
            field=models.DateField(verbose_name='Fecha de asignación: '),
        ),
    ]