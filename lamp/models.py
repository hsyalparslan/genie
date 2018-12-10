from django.db import models
from django.conf import settings
from django.contrib.sessions.models import Session
# Create your models here.


class Lamp(models.Model):
	q_number = models.CharField(max_length=100, default="DEFAULT")
	q_1 = models.CharField(max_length=10000, default="DEFAULT")
	q_2 = models.CharField(max_length=10000, default="DEFAULT")
	q_3 = models.CharField(max_length=10000, default="DEFAULT")
	q_4 = models.CharField(max_length=10000, default="DEFAULT")
	q_5 = models.CharField(max_length=10000, default="DEFAULT")
	q_6 = models.CharField(max_length=10000, default="DEFAULT")
	q_7 = models.CharField(max_length=10000, default="DEFAULT")
	q_8 = models.CharField(max_length=10000, default="DEFAULT")
	q_9 = models.CharField(max_length=10000, default="DEFAULT")
	def publish(self):
		self.save

	def __str__(self):
		return self.q_number



		