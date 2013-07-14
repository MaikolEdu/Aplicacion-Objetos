#from .models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from .forms import *


def inicio(request):
	return render_to_response('inicio.html',context_instance=RequestContext(request))

#---------------------------------------------CLIENTE
#----------------------------------------------------

def registrar_cliente(request):
	if request.method=='POST':
		formulario = ClienteForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = ClienteForm()
	return render_to_response('registrar_cliente.html',{'formulario':formulario},context_instance=RequestContext(request))

def listar_cliente(request):
	usuarios = Cliente.objects.all()
	return render_to_response('listar_cliente.html',{'usuarios':usuarios},context_instance=RequestContext(request))

#-------------------------------------------CONDUCTOR
#----------------------------------------------------

def registrar_conductor(request):
	if request.method=='POST':
		formulario = ConductorForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = ConductorForm()
	return render_to_response('registrar_conductor.html',{'formulario':formulario},context_instance=RequestContext(request))

def listar_conductor(request):
	usuarios = Conductor.objects.all()
	return render_to_response('listar_conductor.html',{'usuarios':usuarios},context_instance=RequestContext(request))

#---------------------------------------RECEPCIONISTA
#----------------------------------------------------

def registrar_recepcionista(request):
	if request.method=='POST':
		formulario = RecepcionistaForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = RecepcionistaForm()
	return render_to_response('registrar_recepcionista.html',{'formulario':formulario},context_instance=RequestContext(request))

def listar_recepcionista(request):
	usuarios = Recepcionista.objects.all()
	return render_to_response('listar_recepcionista.html',{'usuarios':usuarios},context_instance=RequestContext(request))

#--------------------------------------------VEHICULO
#----------------------------------------------------

def registrar_transporte(request):
	if request.method=='POST':
		formulario = VehiculoForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = VehiculoForm()
	return render_to_response('registrar_transporte.html',{'formulario':formulario},context_instance=RequestContext(request))

def listar_transporte(request):
	usuarios = Vehiculo.objects.all()
	return render_to_response('listar_transporte.html',{'usuarios':usuarios},context_instance=RequestContext(request))

#--------------------------------------------VEHICULO
#----------------------------------------------------

def registrar_reclamo(request):
	if request.method=='POST':
		formulario = ReclamoForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = ReclamoForm()
	return render_to_response('registrar_reclamo.html',{'formulario':formulario},context_instance=RequestContext(request))

def listar_reclamo(request):
	usuarios = Reclamo.objects.all()
	print usuarios
	return render_to_response('listar_reclamo.html',{'usuarios':usuarios},context_instance=RequestContext(request))