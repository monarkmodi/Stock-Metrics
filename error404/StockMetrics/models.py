from django.db import models

# Create your models here.

class Stock(model.Model):

	title = models.Charfield(max_length=20)
	id = models.Charfield(max_length=20)
	volume = models.IntegerField()
	buy_price = models.FloatField()
	sell_price = models.FloatField()

	def _str_(self):
		"""
        String for representing the Model object.
        """
		return self.title

class User(model.Model):

	name = models.Charfield(max_length=20)
	date_of_birth = models.DateField()
	email = models.Charfield(max_length=20)
	password = models.Charfield(max_length=20)
	balance = models.FLoatField()

	def _str_(self):
		"""
        String for representing the Model object.
        """
		return self.name

