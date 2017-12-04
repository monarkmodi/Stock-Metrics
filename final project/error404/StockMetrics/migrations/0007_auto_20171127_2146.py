# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StockMetrics', '0006_stockmetrics_metric_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockdata',
            name='funds_available',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockdata',
            name='port_value',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockdata',
            name='profit_loss',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
