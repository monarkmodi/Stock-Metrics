from django.db import models


# Create your models here.

class Stock(models.Model):

	title = models.CharField(max_length=20)
	stock_id = models.IntegerField()
	volume = models.IntegerField()
	buy_price = models.FloatField()
	sell_price = models.FloatField()

	def _str_(self):
		"""
        String for representing the Model object.
        """
		return self.title



class User(models.Model):

	name = models.CharField(max_length=30)
	date_of_birth = models.DateField()
	email = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	balance = models.FloatField()

	def _str_(self):
		"""
        String for representing the Model object.
        """
		return self.name

class StockMetrics(models.Model):

	metrics = (
        ('RSI','Relative Strength Index (RSI)'),
        ('OBV','On Balance Volume (OBV)'),
        ('AI','Aroon Indicator'),
        ('SMA','Simple Moving Average'),
        ('SO','Stochastic Oscillator'),
    )
	
	Metric_Title = models.CharField(max_length=20, choices=metrics, default=metrics[0])
	StockName = models.CharField(max_length=20)

	def _str_(self):
		"""
        String for representing the Model object.
        """
		return self.Metric_Title


class Portfolio(models.Model):

	user = models.CharField(max_length=20)
	portfolio_value = models.FloatField()
	buying_power = models.FloatField()
	withdrawable_cash = models.FloatField()
	cash_balance = models.FloatField()
	invested_fund = models.FloatField()


	def _str_(self):
		"""
        String for representing the Model object.
        """
		return self.user


	def withdrawableCash(self):
		"""
        String for representing the Model object.
        """
		self.withdrawable_cash = self.buying_power - self.invested_fund
		return self.withdrawable_cash





