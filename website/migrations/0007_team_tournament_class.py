# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20150701_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='tournament_class',
            field=models.CharField(choices=[('H', 'Herrer'), ('D', 'Damer'), ('A', 'Åpen')], default='Herrer', max_length=100),
        ),
    ]
