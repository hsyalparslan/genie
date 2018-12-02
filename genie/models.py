from django.db import models
from django.conf import settings
from django.contrib.sessions.models import Session
# Create your models here.


class Activity(models.Model):
	g_name = models.CharField(max_length=20, default="DEFAULT")
	g_choice = models.CharField(max_length=20, default="DEFAULT")
	honeypot = models.CharField(max_length=20, default="DEFAULT")
	def publish(self):
		self.save

	def __str__(self):
		return self.g_name