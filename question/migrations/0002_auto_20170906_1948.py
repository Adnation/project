# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-06 19:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='user_id',
            new_name='user',
        ),
    ]
