# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StockMetrics', '0007_auto_20171127_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('symbol', models.CharField(max_length=5, verbose_name='Symbol')),
                ('number', models.IntegerField()),
                ('openPrice', models.FloatField()),
                ('closePrice', models.FloatField()),
            ],
        ),
    ]
