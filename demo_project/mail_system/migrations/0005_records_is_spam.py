# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail_system', '0004_auto_20170322_1918'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='is_spam',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
