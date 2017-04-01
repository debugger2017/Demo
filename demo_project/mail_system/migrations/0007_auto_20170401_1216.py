# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mail_system', '0006_auto_20170324_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('is_spam', models.BooleanField(default=False)),
                ('from_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='from_user_id')),
                ('to_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='to_user_id')),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User_Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
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
        migrations.AlterUniqueTogether(
            name='records',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='records',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='records',
            name='to_user',
        ),
        migrations.DeleteModel(
            name='Records',
        ),
        migrations.RemoveField(
            model_name='registeredusers',
            name='user',
        ),
        migrations.RemoveField(
            model_name='usermails',
            name='mail',
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
            name='RegisteredUsers',
        ),
        migrations.DeleteModel(
            name='UserMails',
        ),
        migrations.AlterUniqueTogether(
            name='relation',
            unique_together=set([('from_user', 'to_user')]),
        ),
        migrations.RemoveField(
            model_name='mail',
            name='is_read',
        ),
        migrations.RemoveField(
            model_name='mail',
            name='timestamp',
        ),
    ]
