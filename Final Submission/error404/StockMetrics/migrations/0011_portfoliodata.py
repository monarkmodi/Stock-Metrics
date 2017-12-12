# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StockMetrics', '0010_orderdata_totalprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('symbol', models.CharField(max_length=5, verbose_name='Symbol')),
                ('open_price', models.IntegerField()),
                ('high_price', models.FloatField()),
                ('low_price', models.FloatField()),
                ('close_price', models.FloatField()),
                ('volume', models.FloatField()),
            ],
        ),
    ]
