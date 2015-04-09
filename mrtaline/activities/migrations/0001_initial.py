# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import activities.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('slug', models.CharField(max_length=256, blank=True)),
                ('description', models.TextField()),
                ('published', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(upload_to=activities.models.get_upload_filename, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
