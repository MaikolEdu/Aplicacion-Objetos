# encoding:utf-8
from django.db import models

ciudad=(
	('Trujillo','Trujillo'),
	('Pataz','Pataz')
)

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
	lugartrabajo=models.CharField(max_length=10,choices=ciudad)

	def __unicode__(self):
		return "%s" % (self.nombre)

class Conductor(models.Model):
	nombre    = models.CharField(max_length=100)
	direccion = models.CharField(max_length=200)
	dni       = models.CharField(max_length=8)

	def __unicode__(self):
		return "%s" % (self.nombre)

class Vehiculo(models.Model):
	descripcion = models.CharField(max_length=100)
	placa       = models.CharField(max_length=200)
	estadooperativo=models.BooleanField(default=False)

	def __unicode__(self):
		return "%s" % (self.placa)

class Reclamo(models.Model):
	fecha         = models.DateField(auto_now=True)
	descripcion   = models.TextField()
	cliente       = models.ForeignKey(Cliente)
	recepcionista = models.ForeignKey(Recepcionista)

	def __unicode__(self):
		return "%s" % (self.fecha)

class Comprobante(models.Model):
	fecha         = models.DateField(auto_now=True)
	monto         = models.CharField(max_length=10)
	pesototal     = models.CharField(max_length=8)
	recepcionista = models.ForeignKey(Recepcionista)
	cliente       = models.ForeignKey(Cliente)
	ciudad        = models.CharField(max_length=10)
	detalle       = models.TextField()
	estado        = models.BooleanField(default=False)

	def __unicode__(self):
		return "cliente %s con monto de %s" % (self.cliente,self.monto)

class GuiaRemision(models.Model):
	conductor      = models.ForeignKey(Conductor)
	comprobante	   = models.ForeignKey(Comprobante)
	vehiculo       = models.ForeignKey(Vehiculo)
	fechaentrada   = models.DateField(auto_now=True)
	fechasalida    = models.DateField(auto_now=False)
	destino        = models.CharField(max_length=10)
	destinatario   = models.CharField(max_length=100)
	estadoderecojo = models.BooleanField(default=False)

	def __unicode__(self):
		return "conductor %s con monto de %s" % (self.conductor,self.fechasalida)
