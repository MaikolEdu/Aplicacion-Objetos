from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),

	url(r'^$', 'principal.views.inicio'),
	url(r'^cliente/registrar/$', 'principal.views.registrar_cliente'),
	url(r'^cliente/listar/$', 'principal.views.listar_cliente'),
	url(r'^recepcionista/registrar/$', 'principal.views.registrar_recepcionista'),
	url(r'^recepcionista/listar/$', 'principal.views.listar_recepcionista'),
	url(r'^conductor/registrar/$', 'principal.views.registrar_conductor'),
	url(r'^conductor/listar/$', 'principal.views.listar_conductor'),
	url(r'^transporte/registrar/$', 'principal.views.registrar_transporte'),
	url(r'^transporte/listar/$', 'principal.views.listar_transporte'),
	url(r'^reclamo/registrar/$', 'principal.views.registrar_reclamo'),
	url(r'^reclamo/listar/$', 'principal.views.listar_reclamo'),
)
