from django.db import models
from django.conf import settings
from django.contrib.sessions.models import Session
# Create your models here.


class Guess(models.Model):
	c_number = models.CharField(max_length=100, default="DEFAULT")
	c_1 = models.CharField(max_length=10000, default="DEFAULT")
	c_2 = models.CharField(max_length=10000, default="DEFAULT")
	c_3 = models.CharField(max_length=10000, default="DEFAULT")
	c_4 = models.CharField(max_length=10000, default="DEFAULT")
	c_5 = models.CharField(max_length=10000, default="DEFAULT")
	c_6 = models.CharField(max_length=10000, default="DEFAULT")
	def publish(self):
		self.save

	def __str__(self):
		return self.c_number



		