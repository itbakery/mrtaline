# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import businesses.models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biztype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.CharField(max_length=256, blank=True)),
                ('address', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('published', models.BooleanField(default=False)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('photo', models.ImageField(upload_to=businesses.models.get_upload_filename)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('biztypes', models.ManyToManyField(to='businesses.Biztype')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
