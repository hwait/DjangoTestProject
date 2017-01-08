# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 12:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LSChamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LSEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lsid', models.IntegerField()),
                ('dtc', models.DateTimeField(null=True)),
                ('cid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='livescores.LSChamp')),
            ],
        ),
        migrations.CreateModel(
            name='LSGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setn', models.IntegerField()),
                ('sc1', models.IntegerField()),
                ('sc2', models.IntegerField()),
                ('prewin', models.IntegerField()),
                ('dtc', models.DateTimeField(null=True)),
                ('eid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='livescores.LSEvent')),
            ],
        ),
        migrations.CreateModel(
            name='LSPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LSPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sc1', models.IntegerField()),
                ('sc2', models.IntegerField()),
                ('dtc', models.DateTimeField(null=True)),
                ('gid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='livescores.LSGame')),
            ],
        ),
        migrations.AddField(
            model_name='lsevent',
            name='pid1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player1', to='livescores.LSPlayer'),
        ),
        migrations.AddField(
            model_name='lsevent',
            name='pid2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player2', to='livescores.LSPlayer'),
        ),
    ]
