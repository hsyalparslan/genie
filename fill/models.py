from django.db import models
from django.conf import settings
from django.contrib.sessions.models import Session
# Create your models here.


class Fill(models.Model):
	f_number = models.CharField(max_length=100, default="DEFAULT")
	f_1 = models.CharField(max_length=10000, default="DEFAULT")
	f_2 = models.CharField(max_length=10000, default="DEFAULT")
	f_3 = models.CharField(max_length=10000, default="DEFAULT")
	f_4 = models.CharField(max_length=10000, default="DEFAULT")
	f_5 = models.CharField(max_length=10000, default="DEFAULT")
	f_6 = models.CharField(max_length=10000, default="DEFAULT")
	f_7 = models.CharField(max_length=10000, default="DEFAULT")
	f_8 = models.CharField(max_length=10000, default="DEFAULT")
	def publish(self):
		self.save

	def __str__(self):
		return self.f_number



		