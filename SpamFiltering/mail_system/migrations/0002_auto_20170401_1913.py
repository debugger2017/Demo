# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail_system', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mail_information',
            name='mail',
        ),
        migrations.DeleteModel(
            name='Mail',
        ),
        migrations.RemoveField(
            model_name='mail_information',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='mail_information',
            name='sender',
        ),
        migrations.DeleteModel(
            name='Mail_Information',
        ),
        migrations.AlterUniqueTogether(
            name='spammed_sender',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='spammed_sender',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='spammed_sender',
            name='to_user',
        ),
        migrations.DeleteModel(
            name='Spammed_Sender',
        ),
    ]
