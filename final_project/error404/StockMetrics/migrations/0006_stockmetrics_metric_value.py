# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StockMetrics', '0005_stockdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockmetrics',
            name='Metric_value',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
