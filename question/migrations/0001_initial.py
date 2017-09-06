# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-06 17:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_title', models.CharField(max_length=2000)),
                ('is_private', models.BooleanField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]