# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20150701_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='email',
            field=models.CharField(max_length=100, help_text='eksempel@eksempel.no'),
        ),
        migrations.AlterField(
            model_name='team',
            name='other',
            field=models.TextField(max_length=256, blank=True, help_text='Annen informasjon'),
        ),
        migrations.AlterField(
            model_name='team',
            name='phone',
            field=models.CharField(max_length=15, help_text='12345678'),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_from',
            field=models.CharField(max_length=100, help_text='Lag/sted'),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_name',
            field=models.CharField(max_length=100, help_text='Lagnavn'),
        ),
    ]
