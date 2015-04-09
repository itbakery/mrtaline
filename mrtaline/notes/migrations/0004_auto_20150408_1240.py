# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20150408_1239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='msatypes',
            new_name='msgtypes',
        ),
    ]
