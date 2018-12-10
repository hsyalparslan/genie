from django.db import models
from django.conf import settings
from django.contrib.sessions.models import Session
# Create your models here.


class Poem(models.Model):
	p_number = models.CharField(max_length=100, default="DEFAULT")
	p_1 = models.CharField(max_length=1000, default="DEFAULT")
	p_2 = models.CharField(max_length=1000, default="DEFAULT")
	p_3 = models.CharField(max_length=1000, default="DEFAULT")
	def publish(self):
		self.save

	def __str__(self):
		return self.p_number



		