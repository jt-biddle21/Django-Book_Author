# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-14 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bkau_app', '0004_auto_20171114_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default=0),
        ),
    ]