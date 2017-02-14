# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeredusers',
            name='city',
            field=models.CharField(max_length=10, default='sangli'),
            preserve_default=False,
        ),
    ]
