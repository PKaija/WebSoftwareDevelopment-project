# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-02-07 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=3, max_digits=5)),
                ('description', models.TextField()),
                ('url', models.URLField(default=b'')),
            ],
        ),
    ]
