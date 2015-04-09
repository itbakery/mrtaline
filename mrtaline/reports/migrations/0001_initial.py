# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields
from django.conf import settings
import uuidfield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('uuid', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, blank=True)),
                ('description', models.TextField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('user', models.ForeignKey(related_name='areas', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('slug', models.CharField(max_length=256, blank=True)),
                ('uuid', uuidfield.fields.UUIDField(unique=True, max_length=32, editable=False, blank=True)),
                ('description', models.TextField()),
                ('published', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('stop_date', models.DateTimeField(auto_now_add=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('picture', models.ImageField(upload_to=b'places/%Y/%m/%d', blank=True)),
                ('status', models.CharField(max_length=1, choices=[(b'd', b'Draft'), (b'p', b'Published'), (b'u', b'UnPublished')])),
                ('reporttype', models.CharField(max_length=1, choices=[(b't', b'Traffic'), (b'c', b'Contruction'), (b'b', b'Block'), (b'v', b'Vibration'), (b'w', b'Water')])),
                ('categories', models.ManyToManyField(to='reports.Category', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Portal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('user', models.ForeignKey(related_name='portals', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='place',
            name='portal',
            field=models.ForeignKey(related_name='portals', blank=True, to='reports.Portal'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='place',
            name='user',
            field=models.ForeignKey(related_name='places', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
