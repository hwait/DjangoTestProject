# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betfair_app', '0008_auto_20170117_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='bfchamp',
            name='mcid',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='bfevent',
            name='meid',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='bfplayer',
            name='mpid',
            field=models.IntegerField(null=True),
        ),
    ]
