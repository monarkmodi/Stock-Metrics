# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('StockMetrics', '0002_auto_20171127_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='buy_price',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='sell_price',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='stock_id',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='title',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='volume',
        ),
        migrations.AlterField(
            model_name='stock',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
