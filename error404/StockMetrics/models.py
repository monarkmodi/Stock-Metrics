from django.db import models

# Create your models here.

class Stock(models.Model):

	title = models.CharField(max_length=20)
	ID = models.CharField(max_length=20)
	volume = models.IntegerField()
	buy_price = models.FloatField()
	sell_price = models.FloatField()

	def _str_(self):
		"""
        String for representing the Model object.
        """
		return self.title

class User(models.Model):

	name = models.CharField(max_length=20)
	date_of_birth = models.DateField()
	email = models.CharField(max_length=20)
	password = models.CharField(max_length=20)
	balance = models.FloatField()

	def _str_(self):
		"""
        String for representing the Model object.
        """
		return self.name
