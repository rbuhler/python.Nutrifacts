# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-06 16:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facts', '0004_auto_20170606_1302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nutrifact',
            old_name='id',
            new_name='key',
        ),
        migrations.RenameField(
            model_name='nutritable',
            old_name='id',
            new_name='key',
        ),
    ]
