# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StockMetrics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='user',
            field=models.IntegerField(null=True),
        ),
    ]
