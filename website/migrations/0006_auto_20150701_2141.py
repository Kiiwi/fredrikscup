# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_register'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Register',
            new_name='Team',
        ),
    ]
