# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StockMetrics', '0009_orderdata_profit'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdata',
            name='totalPrice',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
