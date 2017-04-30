# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail_system', '0003_auto_20170402_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spammed_sender',
            name='is_sender_spam',
            field=models.IntegerField(default=0),
        ),
    ]
