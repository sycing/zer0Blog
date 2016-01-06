# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 04:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('view_count', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-publish_time'],
            },
        ),
    ]
