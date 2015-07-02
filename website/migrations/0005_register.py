# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_delete_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('team_name', models.CharField(max_length=100)),
                ('team_from', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
