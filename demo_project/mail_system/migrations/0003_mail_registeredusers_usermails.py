# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mail_system', '0002_auto_20170302_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('subject', models.CharField(max_length=256)),
                ('content', models.CharField(max_length=4096)),
                ('is_spam', models.BooleanField(default=False)),
                ('is_read', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True, unique=True)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RegisteredUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('mobile', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=10)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserMails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('mail', models.ForeignKey(to='mail_system.Mail')),
                ('receiver', models.ForeignKey(related_name='receiver_id', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(related_name='sender_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
    ]
