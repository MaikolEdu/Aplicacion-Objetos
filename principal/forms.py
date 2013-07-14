#encoding:utf-8
from django.forms import ModelForm
from django import forms
from .models import *


class ClienteForm(ModelForm):
	class Meta:
		model= Cliente