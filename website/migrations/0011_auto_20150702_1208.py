# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20150702_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='registration',
            name='other',
            field=models.TextField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='registration',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='registration',
            name='team_from',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='registration',
            name='team_name',
            field=models.CharField(max_length=100),
        ),
    ]
