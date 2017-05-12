# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail_system', '0006_spammed_sender_is_sender_spam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spammed_sender',
            name='is_sender_spam',
        ),
    ]
