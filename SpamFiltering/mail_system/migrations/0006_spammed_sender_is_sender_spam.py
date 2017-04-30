# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail_system', '0005_remove_spammed_sender_is_sender_spam'),
    ]

    operations = [
        migrations.AddField(
            model_name='spammed_sender',
            name='is_sender_spam',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
