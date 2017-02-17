# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 08:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oddsportal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OPChamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lid', models.IntegerField(null=True)),
                ('sport', models.IntegerField()),
                ('country', models.CharField(max_length=30)),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OPEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lid', models.IntegerField(null=True)),
                ('meid', models.IntegerField(null=True)),
                ('reversed', models.IntegerField(null=True)),
                ('sets1', models.IntegerField(null=True)),
                ('sets2', models.IntegerField(null=True)),
                ('dt', models.DateTimeField(null=True)),
                ('dtc', models.DateTimeField(null=True)),
                ('result', models.IntegerField(null=True)),
                ('champ', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='oddsportal.OPChamp')),
            ],
        ),
        migrations.CreateModel(
            name='OPOdds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w1', models.FloatField(db_index=True, null=True)),
                ('w2', models.FloatField(db_index=True, null=True)),
                ('w1max', models.FloatField(db_index=True, null=True)),
                ('w2max', models.FloatField(db_index=True, null=True)),
                ('dtc', models.DateTimeField(null=True)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='oddsportal.OPEvent')),
            ],
        ),
        migrations.CreateModel(
            name='OPPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lid', models.IntegerField(null=True)),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('gender', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='OPMeet',
        ),
        migrations.AddField(
            model_name='opevent',
            name='p1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opplayer1', to='oddsportal.OPPlayer'),
        ),
        migrations.AddField(
            model_name='opevent',
            name='p2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opplayer2', to='oddsportal.OPPlayer'),
        ),
    ]