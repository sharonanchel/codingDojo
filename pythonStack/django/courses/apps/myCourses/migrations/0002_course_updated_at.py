# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-29 01:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myCourses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]