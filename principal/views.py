#from .models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from .forms import *


def inicio(request):
	return render_to_response('inicio.html',context_instance=RequestContext(request))


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