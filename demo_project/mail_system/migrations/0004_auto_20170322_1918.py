# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mail_system', '0003_mail_registeredusers_usermails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('mail_count', models.IntegerField(default=0)),
                ('from_user', models.ForeignKey(related_name='from_user_id', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(related_name='to_user_id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='records',
            unique_together=set([('from_user', 'to_user')]),
        ),
    ]
