# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-18 19:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pills',
            name='id_medic',
        ),
        migrations.RemoveField(
            model_name='pills',
            name='id_ph',
        ),
        migrations.DeleteModel(
            name='Medic',
        ),
        migrations.DeleteModel(
            name='Pharmacy',
        ),
        migrations.DeleteModel(
            name='Pills',
        ),
    ]