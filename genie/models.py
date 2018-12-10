from django.db import models
from django.conf import settings
from django.contrib.sessions.models import Session
# Create your models here.


class TaskTwoGenie(models.Model):
	g_name = models.CharField(max_length=100, default="DEFAULT")
	g_choice = models.CharField(max_length=10000, default="DEFAULT")
	wishes = models.CharField(max_length=1000, default="DEFAULT")
	honeypot = models.CharField(max_length=20, default="DEFAULT")
	def publish(self):
		self.save

	def __str__(self):
		return self.g_name


class TaskTwoCustomer(models.Model):
	c_name = models.CharField(max_length=50)
	c_wish = models.CharField(max_length=1000)

	def __str__(self):
		return self.c_name

		