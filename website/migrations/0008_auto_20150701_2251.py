# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_team_tournament_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='other',
            field=models.TextField(max_length=256, blank=True),
        ),
        migrations.AddField(
            model_name='team',
            name='phone',
            field=models.CharField(max_length=15, default=12345678),
            preserve_default=False,
        ),
    ]
