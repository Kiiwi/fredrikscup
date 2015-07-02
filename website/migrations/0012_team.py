# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20150702_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('team_name', models.CharField(max_length=100)),
                ('team_from', models.CharField(max_length=100)),
                ('tournament_class', models.CharField(default='Herrer', choices=[('H', 'Herrer'), ('D', 'Damer'), ('A', 'Åpen')], max_length=100)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
