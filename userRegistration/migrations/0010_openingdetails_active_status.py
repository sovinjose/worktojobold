# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-09 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRegistration', '0009_openingdetails_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='openingdetails',
            name='active_status',
            field=models.BooleanField(default=True),
        ),
    ]
