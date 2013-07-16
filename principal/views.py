#from .models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from .forms import *
from datetime import date
from django.utils import simplejson as json
from django.core import serializers

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

#-----------------------------------------COMPROBANTE
#----------------------------------------------------
def registrar_comprobante(request):
	fecha= date.today()
	contador=Comprobante.objects.all().count() +1
	if request.method=='POST':
		formulario = ComprobanteForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else:
		formulario = ComprobanteForm()
	return render_to_response('registrar_comprobante.html',{'formulario':formulario,'fecha':fecha ,'contador':contador},context_instance=RequestContext(request))

def listar_comprobante(request):
	usuarios = Comprobante.objects.all()
	return render_to_response('listar_comprobante.html',{'usuarios':usuarios},context_instance=RequestContext(request))



#-----------------------------------GUIA-----REMISION
#----------------------------------------------------
def registrar_guiaremision(request):
	fecha= date.today()
	contador=GuiaRemision.objects.all().count() +1
	comprobantes=Comprobante.objects.filter(estado=0)
	if request.method=='POST':
		formulario = GuiaRemisionForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			alterarcomprobante= Comprobante.objects.get(pk=request.POST['comprobante'])
			alterarcomprobante.estado=1
			alterarcomprobante.save()
			return HttpResponseRedirect('/')
	else:
		formulario = GuiaRemisionForm()
	return render_to_response('registrar_guiaremision.html',{'formulario':formulario,'comprobante':comprobantes,'fecha':fecha ,'contador':contador},context_instance=RequestContext(request))

def listar_guiaremision(request):
	usuarios = GuiaRemision.objects.all()
	return render_to_response('listar_guiaremision.html',{'usuarios':usuarios},context_instance=RequestContext(request))





def reporte_grafico(request):
	comprobantes= Comprobante.objects.all()
	fecha_actual = date.today()
	meses = {1:'Ene', 2:'Feb', 3:'Mar', 4:'Abr', 5:'May', 6:'Jun',
			 7:'Jul', 8:'Ago', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dic'}
	mi_data=[]
	for key,item in meses.iteritems():
		grafico_mes=comprobantes.filter(fecha__year=fecha_actual.year,fecha__month=key)
		suma=0.00
		for indice2,elemento2 in enumerate(grafico_mes):
			suma= suma + float(elemento2.monto)
		mi_data.append({'mes':item,
						'cantidad':suma,		
						})
	print mi_data
	return render_to_response('reporte_grafico.html',{'datos':mi_data},context_instance=RequestContext(request))

#-----------------------------LLAMADOS AJAX----------
#----------------------------------------------------
def ajax_ver_recepcionista(request):	
	if request.is_ajax():
		clave=request.GET['id_recepcionista']
		usuario = Recepcionista.objects.get(pk=clave) 
		data=json.dumps({'ciudad':usuario.lugartrabajo})

		return HttpResponse(data, mimetype="application/json")
	else:
		raise Http404


#para chekear de que ciudad pertenece dicho comprobante emitido
def ajax_ver_comprobante(request):	
	if request.is_ajax():
		clave=request.GET['id_comprobante']
		comprobantes = Comprobante.objects.get(pk=clave)
		if comprobantes.ciudad=='Trujillo':
			ciudad='Pataz'
		else:
			ciudad='Trujillo'
		data=json.dumps({'ciudad':ciudad})

		return HttpResponse(data, mimetype="application/json")
	else:
		raise Http404

