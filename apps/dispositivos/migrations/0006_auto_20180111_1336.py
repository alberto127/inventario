# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-11 12:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivos', '0005_auto_20180111_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='fecha_instalacion',
            field=models.DateField(default=datetime.date(2018, 1, 11), verbose_name='Fecha de asignación: '),
        ),
    ]
