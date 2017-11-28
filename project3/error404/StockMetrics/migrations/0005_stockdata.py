# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StockMetrics', '0004_auto_20171127_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('stock_id', models.IntegerField()),
                ('volume', models.IntegerField()),
                ('buy_price', models.FloatField()),
                ('sell_price', models.FloatField()),
            ],
        ),
    ]
