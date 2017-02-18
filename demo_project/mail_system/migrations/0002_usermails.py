# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mail_id', models.ForeignKey(to='mail_system.Mail')),
                ('receiver_id', models.ForeignKey(to='mail_system.RegisteredUsers', related_name='receiver_id')),
                ('sender_id', models.ForeignKey(to='mail_system.RegisteredUsers', related_name='sender_id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
