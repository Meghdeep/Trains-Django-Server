# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20150419_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='menu',
            field=models.CharField(max_length=200),
        ),
    ]
