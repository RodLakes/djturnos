from __future__ import unicode_literals
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from jornadas import views


urlpatterns = [
#General    
    url(r'^panel/$', views.Panel, name="panel"),
    url(r'^listarempleados/$', views.Empleados, name='empleados'),
    url(r'^asistencias/$', views.AsistenciaLista, name='asistencias'),
#asistencias 
    url(r'^eliminarasistencias/(?P<item>\d+)$', views.EliminarAsistencia, name='eliminarasistencia'),
    url(r'^editasistencia/(?P<item>\d+)$', views.AsistenciaEditar, name='editasistencia'),
#turnos
    url(r'^turnos/$', views.TurnoLista, name='turnos'),    
    url(r'^eliminaturno/(?P<item>\d+)$', views.EliminaTurno, name='eliminaturno'),
    url(r'^editaturno/(?P<item>\d+)$', views.EditaTurno, name='editaturno'),
#empleados
    url(r'^editar/(?P<item>\d+)$', views.Empleados_editar, name="empleados_editar"),
    url(r'^regentidad/$', views.RegistrarEntidad, name='addentidad'),
    url(r'^fotos/(?P<id_entidad>\d+)$', views.Captura, name='guardar_imagen'),
#jornada
    url(r'^jornadas/$', views.JornadaLista, name='jornadas'),    
    url(r'^eliminajornada/(?P<item>\d+)$', views.EliminaJornada, name='eliminajornada'),
    url(r'^editajornada/(?P<item>\d+)$', views.EditaJornada, name='editajornada'),

]
