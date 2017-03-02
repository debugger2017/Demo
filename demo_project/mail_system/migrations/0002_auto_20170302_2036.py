# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail_system', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registeredusers',
            name='user',
        ),
        migrations.DeleteModel(
            name='RegisteredUsers',
        ),
        migrations.RemoveField(
            model_name='usermails',
            name='mail',
        ),
        migrations.DeleteModel(
            name='Mail',
        ),
        migrations.RemoveField(
            model_name='usermails',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='usermails',
            name='sender',
        ),
        migrations.DeleteModel(
            name='UserMails',
        ),
    ]
