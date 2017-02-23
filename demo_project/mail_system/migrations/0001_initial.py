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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('mail_id', models.ForeignKey(to='mail_system.Mail')),
                ('receiver_id', models.ForeignKey(related_name='receiver_id', to=settings.AUTH_USER_MODEL)),
                ('sender_id', models.ForeignKey(related_name='sender_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
