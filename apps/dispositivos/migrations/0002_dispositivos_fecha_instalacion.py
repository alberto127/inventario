# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-10 10:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispositivos',
            name='fecha_instalacion',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 10, 11, 48, 8, 700492), verbose_name='Fecha de asignación: '),
        ),
    ]
