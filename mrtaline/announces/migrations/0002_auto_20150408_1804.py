# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announces', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announce',
            name='published',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='announce',
            name='modified',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
