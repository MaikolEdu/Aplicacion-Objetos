# encoding:utf-8
from django.db import models

class Cliente(models.Model):
	nombre    = models.CharField(max_length=100)
	direccion = models.CharField(max_length=200)
	dni       = models.CharField(max_length=8)
	ruc       = models.CharField(max_length=11)

	def __unicode__(self):
		return "%s" % (self.nombre)
