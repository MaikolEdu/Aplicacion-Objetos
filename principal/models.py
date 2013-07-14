# encoding:utf-8
from django.db import models

class Cliente(models.Model):
	nombre    = models.CharField(max_length=100)
	direccion = models.CharField(max_length=200)
	dni       = models.CharField(max_length=8)
	ruc       = models.CharField(max_length=11)

	def __unicode__(self):
		return "%s" % (self.nombre)


class Recepcionista(models.Model):
	nombre    = models.CharField(max_length=100)
	direccion = models.CharField(max_length=200)
	dni       = models.CharField(max_length=8)
	ruc       = models.CharField(max_length=11)

	def __unicode__(self):
		return "%s" % (self.nombre)

class Conductor(models.Model):
	nombre    = models.CharField(max_length=100)
	direccion = models.CharField(max_length=200)
	dni       = models.CharField(max_length=8)
	ruc       = models.CharField(max_length=11)

	def __unicode__(self):
		return "%s" % (self.nombre)

class Vehiculo(models.Model):
	descripcion = models.CharField(max_length=100)
	placa       = models.CharField(max_length=200)

	def __unicode__(self):
		return "%s" % (self.placa)

class Reclamo(models.Model):
	fecha= models.DateField(auto_now=True)
	descripcion=models.TextField()
	cliente=models.ForeignKey(Cliente)
	recepcionista=models.ForeignKey(Recepcionista)

	def __unicode__(self):
		return "%s" % (self.fecha)

