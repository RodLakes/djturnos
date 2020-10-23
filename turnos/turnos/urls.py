from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets
from jornadas.viewsets import AsistenciaViewSet, EntidadViewSet, UsuarioViewSet, TurnoViewSet, JornadaViewSet
from django.conf.urls.static import static
from django.conf import settings

# creamos nuestra funcion router de la api y que se vinculara a las urls a crear
rutasapp = DefaultRouter()
rutasapp.register(r'asistencia', AsistenciaViewSet)
rutasapp.register(r'entidad', EntidadViewSet)
rutasapp.register(r'usuario', UsuarioViewSet)
rutasapp.register(r'turno', TurnoViewSet)
rutasapp.register(r'jornada', JornadaViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(rutasapp.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
   # url(r'', include('jornadas.urls', namespace="jornads")),
    path('', include('jornadas.urls')),


]
