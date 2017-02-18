# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail_system', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermails',
            old_name='mail_id',
            new_name='mail',
        ),
        migrations.RenameField(
            model_name='usermails',
            old_name='receiver_id',
            new_name='receiver',
        ),
        migrations.RenameField(
            model_name='usermails',
            old_name='sender_id',
            new_name='sender',
        ),
    ]
