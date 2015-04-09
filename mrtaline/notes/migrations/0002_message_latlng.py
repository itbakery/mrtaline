# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='latlng',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
