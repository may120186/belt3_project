# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-21 05:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logreg_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travel',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='travel',
            name='joined_by',
        ),
        migrations.DeleteModel(
            name='Travel',
        ),
    ]
