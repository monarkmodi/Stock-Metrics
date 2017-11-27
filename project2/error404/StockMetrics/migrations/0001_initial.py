# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=20)),
                ('portfolio_value', models.FloatField()),
                ('buying_power', models.FloatField()),
                ('withdrawable_cash', models.FloatField()),
                ('cash_balance', models.FloatField()),
                ('invested_fund', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('symbol', models.CharField(max_length=5, verbose_name='Symbol')),
                ('title', models.CharField(max_length=20)),
                ('stock_id', models.IntegerField()),
                ('volume', models.IntegerField()),
                ('buy_price', models.FloatField()),
                ('sell_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='StockMetrics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Metric_Title', models.CharField(default=(b'RSI', b'Relative Strength Index (RSI)'), max_length=20, choices=[(b'RSI', b'Relative Strength Index (RSI)'), (b'OBV', b'On Balance Volume (OBV)'), (b'AI', b'Aroon Indicator'), (b'SMA', b'Simple Moving Average'), (b'SO', b'Stochastic Oscillator')])),
                ('StockName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('email', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('balance', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='stock',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
