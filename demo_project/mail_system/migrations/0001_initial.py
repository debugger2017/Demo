# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
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
    ]
