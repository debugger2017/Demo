# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail_system', '0005_records_is_spam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='from_user',
            field=models.ForeignKey(to='mail_system.RegisteredUsers', related_name='from_user_id'),
        ),
        migrations.AlterField(
            model_name='records',
            name='to_user',
            field=models.ForeignKey(to='mail_system.RegisteredUsers', related_name='to_user_id'),
        ),
        migrations.AlterField(
            model_name='usermails',
            name='receiver',
            field=models.ForeignKey(to='mail_system.RegisteredUsers', related_name='receiver_id'),
        ),
        migrations.AlterField(
            model_name='usermails',
            name='sender',
            field=models.ForeignKey(to='mail_system.RegisteredUsers', related_name='sender_id'),
        ),
    ]
