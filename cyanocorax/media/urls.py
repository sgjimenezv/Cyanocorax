from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('media.views',
    url(r'^$', 'pruebaSuma', name='prueba_suma'),
    url(r'^convertir-audio/$', 'convertirAudio', name='convertir_audio'),
    url(r'^stremer-audio/(?P<id_audio>\d+)$', 'stremerAudio',name='stremer_audio'),
    url(r'^convertir-audio/(?P<id_audio>\d+)/(?P<formato>\d+)$', 'stremerAudio',name='stremer_audio'),
    url(r'^formulario-collection/$', 'crear_coleccion',name='formulario_registro_coleccion'),


    #url(r'^do_task$', 'testcele.cele.views.do_task', name='do_task'),
    #url(r'^poll_state$', 'testcele.cele.views.poll_state', name='poll_state'),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)