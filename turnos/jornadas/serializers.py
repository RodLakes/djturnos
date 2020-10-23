from rest_framework import serializers
from django.contrib.auth.models import User
# Importar los modelos
from .models import (Asistencia, Entidad, Usuario, Turno, Jornada)


class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = ('__all__')  # Selecciono todos los campos del modelo __all__


class EntidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entidad  # indicamos el modelo a serializar (tabla)
        fields = ('__all__')  # Selecciono todos los campos del modelo __all__


class UsuarioSerializer(serializers.ModelSerializer):
    # creamos campo nuevo que solo se lee al serializar.
    #sector = serializers.ReadOnlyField(source='vsec_id.vsec_descripcion')

    class Meta:
        model = Usuario  # indicamos el modelo a serializar (tabla)
        fields = ('__all__')  # Selecciono todos los campos del modelo __all__


class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno  # indicamos el modelo a serializar (tabla)
        fields = ('__all__')  # Selecciono todos los campos del modelo __all__


class JornadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jornada  # indicamos el modelo a serializar (tabla)
        fields = ('__all__')  # Selecciono todos los campos del modelo __all__


