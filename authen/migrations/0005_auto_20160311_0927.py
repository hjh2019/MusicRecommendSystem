# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-11 09:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0004_auto_20160311_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumuser',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 11, 9, 27, 12, 517867, tzinfo=utc)),
        ),
    ]
