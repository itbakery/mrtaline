# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_remove_place_portal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='modified',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='place',
            name='reporttype',
            field=models.CharField(max_length=1, choices=[(b't', b'Traffic Jam'), (b'c', b'Contruction'), (b'b', b'Traffic Close'), (b'v', b'Vibration'), (b'w', b'Water'), (b'n', b'Noise'), (b'd', b'Dust')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='place',
            name='status',
            field=models.CharField(default=b'd', max_length=1, choices=[(b'd', b'Draft'), (b'p', b'Published'), (b'u', b'UnPublished')]),
            preserve_default=True,
        ),
    ]
