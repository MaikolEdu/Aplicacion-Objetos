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


)
