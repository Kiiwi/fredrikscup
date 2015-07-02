# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('ingredients', models.TextField(max_length=200, help_text='Put the ingredients required for the recepies here !')),
                ('instructions', models.TextField(max_length=500)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
