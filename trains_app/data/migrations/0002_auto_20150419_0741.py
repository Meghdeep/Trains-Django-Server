# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cab_order',
            name='destination_id',
        ),
        migrations.RemoveField(
            model_name='cab_order',
            name='station_id',
        ),
        migrations.RemoveField(
            model_name='cab_order',
            name='taxi_id',
        ),
        migrations.RemoveField(
            model_name='cab_order',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='route',
            name='station_id',
        ),
        migrations.RemoveField(
            model_name='route',
            name='train_no',
        ),
        migrations.RemoveField(
            model_name='taxi',
            name='station_id',
        ),
        migrations.DeleteModel(
            name='Taxi',
        ),
        migrations.RemoveField(
            model_name='food_order',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='passenger',
            name='cab_order_id',
        ),
        migrations.DeleteModel(
            name='Cab_Order',
        ),
        migrations.RemoveField(
            model_name='passenger',
            name='notification_id',
        ),
        migrations.RemoveField(
            model_name='passenger',
            name='route_id',
        ),
        migrations.DeleteModel(
            name='Route',
        ),
        migrations.AddField(
            model_name='vendor',
            name='menu',
            field=models.CharField(max_length=200, default='1. Idly-20 2. Dosa-20 3. Milk-10 4. Curd Rice-30'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='passenger',
            name='passenger_destination',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Destination',
        ),
        migrations.AlterField(
            model_name='station',
            name='station_id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
