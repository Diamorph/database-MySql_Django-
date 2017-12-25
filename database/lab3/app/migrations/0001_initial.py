# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-21 20:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('lisense', models.CharField(max_length=30)),
                ('about', models.CharField(max_length=30)),
                ('cooperation', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('lisense', models.CharField(max_length=30)),
                ('day_and_night', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('consist', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('medic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Medic')),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Pharmacy')),
            ],
        ),
    ]
