#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import *


class ClienteForm(ModelForm):
	class Meta:
		model= Cliente

class RecepcionistaForm(ModelForm):
	class Meta:
		model= Recepcionista

class ConductorForm(ModelForm):
	class Meta:
		model= Conductor

class VehiculoForm(ModelForm):
	class Meta:
		model= Vehiculo

class ReclamoForm(ModelForm):
	class Meta:
		model= Reclamo