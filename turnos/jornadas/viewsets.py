from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Asistencia, Entidad, Usuario, Turno, Jornada

from .serializers import AsistenciaSerializer, EntidadSerializer, UsuarioSerializer, TurnoSerializer, JornadaSerializer


class AsistenciaViewSet(viewsets.ModelViewSet):

    serializer_class = AsistenciaSerializer
    queryset = Asistencia.objects.all()


class EntidadViewSet(viewsets.ModelViewSet):

    serializer_class = EntidadSerializer
    queryset = Entidad.objects.all()


class UsuarioViewSet(viewsets.ModelViewSet):

    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()


class TurnoViewSet(viewsets.ModelViewSet):

    serializer_class = TurnoSerializer
    queryset = Turno.objects.all()


class JornadaViewSet(viewsets.ModelViewSet):

    serializer_class = JornadaSerializer
    queryset = Jornada.objects.all()
