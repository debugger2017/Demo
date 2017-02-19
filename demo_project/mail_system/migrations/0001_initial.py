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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('subject', models.CharField(max_length=256)),
                ('content', models.CharField(max_length=4096)),
                ('is_spam', models.BooleanField(default=False)),
                ('is_read', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(unique=True, auto_now_add=True)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RegisteredUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('mobile', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=10)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserMails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('mail', models.ForeignKey(to='mail_system.Mail')),
                ('receiver', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='receiver_id')),
                ('sender', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='sender_id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
