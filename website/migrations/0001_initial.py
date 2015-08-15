# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('team_name', models.CharField(max_length=100)),
                ('team_from', models.CharField(max_length=100)),
                ('tournament_class', models.CharField(default='Herrer', max_length=100, choices=[('H', 'Herrer'), ('D', 'Damer'), ('A', 'Åpen')])),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('other', models.TextField(max_length=256, blank=True)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('team_name', models.CharField(max_length=100)),
                ('team_from', models.CharField(max_length=100)),
                ('tournament_class', models.CharField(default='Herrer', max_length=100, choices=[('H', 'Herrer'), ('D', 'Damer'), ('A', 'Åpen')])),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TournamentStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('signup', models.BooleanField(default=True)),
                ('pre_start', models.BooleanField()),
                ('started', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Tournament Status',
                'verbose_name_plural': 'Tournament Status',
            },
        ),
    ]
