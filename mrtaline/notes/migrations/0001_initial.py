# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import notes.models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
                ('message', models.TextField()),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('photo', models.ImageField(upload_to=notes.models.get_upload_filename)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
