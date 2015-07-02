# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_delete_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('ingredients', models.TextField(help_text='Put the ingredients required for the recepies here !', max_length=200)),
                ('instructions', models.TextField(max_length=500)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
