# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('subject', models.CharField(max_length=256)),
                ('content', models.CharField(max_length=4096)),
                ('is_spam', models.BooleanField(default=False)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mail_Information',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('is_read', models.BooleanField(default=False)),
                ('mail', models.ForeignKey(to='mail_system.Mail')),
                ('receiver', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='receiver_id')),
                ('sender', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='sender_id')),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Spammed_Sender',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('is_spam', models.BooleanField(default=False)),
                ('from_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='from_user_id')),
                ('to_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='to_user_id')),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='spammed_sender',
            unique_together=set([('from_user', 'to_user')]),
        ),
    ]
