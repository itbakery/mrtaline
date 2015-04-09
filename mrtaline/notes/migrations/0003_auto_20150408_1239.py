# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_message_latlng'),
    ]

    operations = [
        migrations.CreateModel(
            name='Msgtype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='message',
            name='msatypes',
            field=models.ManyToManyField(to='notes.Msgtype'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='message',
            name='published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='latlng',
            field=models.CharField(default=datetime.datetime(2015, 4, 8, 12, 39, 47, 751740, tzinfo=utc), max_length=250, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(max_length=250),
            preserve_default=True,
        ),
    ]
