# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20150701_2307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('team_name', models.CharField(max_length=100, help_text='Lagnavn')),
                ('team_from', models.CharField(max_length=100, help_text='Lag/sted')),
                ('tournament_class', models.CharField(default='Herrer', max_length=100, choices=[('H', 'Herrer'), ('D', 'Damer'), ('A', 'Åpen')])),
                ('email', models.CharField(max_length=100, help_text='eksempel@eksempel.no')),
                ('phone', models.CharField(max_length=15, help_text='12345678')),
                ('other', models.TextField(blank=True, max_length=256, help_text='Annen informasjon')),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
