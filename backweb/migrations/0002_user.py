# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-06 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('truename', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=10)),
                ('tel', models.CharField(max_length=11)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
