# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-07 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRegistration', '0002_auto_20170222_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='contact_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='cmpny_logo'),
        ),
    ]
