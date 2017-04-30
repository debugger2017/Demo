# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail_system', '0004_auto_20170429_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spammed_sender',
            name='is_sender_spam',
        ),
    ]
