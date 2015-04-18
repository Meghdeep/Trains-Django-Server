# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cab_Order',
            fields=[
                ('cab_order_id', models.AutoField(primary_key=True, serialize=False)),
                ('pickup', models.DateTimeField(verbose_name='Pickup Date Time')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('destination_id', models.AutoField(primary_key=True, serialize=False)),
                ('destination_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Food_Order',
            fields=[
                ('food_order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_made', models.CharField(max_length=200)),
                ('menu', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('pnr', models.CharField(primary_key=True, serialize=False, max_length=200)),
                ('notification_id', models.CharField(max_length=200)),
                ('cab_order_id', models.ForeignKey(to='data.Cab_Order')),
                ('food_order_id', models.ForeignKey(to='data.Food_Order')),
                ('passenger_destination', models.ForeignKey(to='data.Destination')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('route_id', models.CharField(primary_key=True, serialize=False, max_length=200)),
                ('seq_no', models.CharField(max_length=200)),
                ('arrival_time', models.DateTimeField(verbose_name='Arrival Date Time')),
                ('departure_time', models.DateTimeField(verbose_name='Departure Date Time')),
                ('delay', models.TimeField(verbose_name='Delay Time')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('station_id', models.CharField(primary_key=True, serialize=False, max_length=200)),
                ('station_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Taxi',
            fields=[
                ('taxi_no', models.CharField(primary_key=True, serialize=False, max_length=200)),
                ('rate', models.CharField(max_length=200)),
                ('station_id', models.ForeignKey(to='data.Station')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('train_no', models.CharField(primary_key=True, serialize=False, max_length=200)),
                ('train_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(primary_key=True, serialize=False, max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('user_password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('vendor_id', models.CharField(primary_key=True, serialize=False, max_length=200)),
                ('shop_name', models.CharField(max_length=200)),
                ('station_id', models.ForeignKey(to='data.Station')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='route',
            name='station_id',
            field=models.ForeignKey(to='data.Station'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='route',
            name='train_no',
            field=models.ForeignKey(to='data.Train'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='passenger',
            name='passenger_source',
            field=models.ForeignKey(to='data.Station'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='passenger',
            name='route_id',
            field=models.ForeignKey(to='data.Route'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='passenger',
            name='user_id',
            field=models.ForeignKey(to='data.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='food_order',
            name='user_id',
            field=models.ForeignKey(to='data.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='food_order',
            name='vendor_id',
            field=models.ForeignKey(to='data.Vendor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cab_order',
            name='destination_id',
            field=models.ForeignKey(to='data.Destination'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cab_order',
            name='station_id',
            field=models.ForeignKey(to='data.Station'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cab_order',
            name='taxi_id',
            field=models.ForeignKey(to='data.Taxi'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cab_order',
            name='user_id',
            field=models.ForeignKey(to='data.User'),
            preserve_default=True,
        ),
    ]
