# coding=utf-8
from django import forms
from django.contrib.auth.forms import User
from django.db import models
from .models import *
from django.utils.translation import gettext as _


class EntidadForm(forms.ModelForm):
    class Meta:
        model = Entidad
        fields = "__all__"
        labels = {
            'id_entidad': 'Registro N°',
            'rut': 'Rut / DNI',
            'nombres': 'Nombre',
            'apellido_pat': 'Apellido Paterno',
            'apellido_mat': 'Apellido Materno',
            'direccion': 'Direccion',
            'telefono': 'Telefono',
            'email': 'Email',
        }
        widgets = {
            'id_entidad': forms.TextInput(attrs={
                "type": "text",
                "size": "5",
                "placeholder": _("Escriba su Rut"),
            }),
            'rut': forms.TextInput(attrs={
                "type": "text",
                "size": "10",
                "placeholder": _("Escriba su Rut"),
            }),
            'nombres': forms.TextInput(attrs={
                "type": "text",
                "size": "25",
                "placeholder": _("Escriba su nombre"),
            }),
            'apellido_pat': forms.TextInput(attrs={
                "type": "text",
                "size": "20",
                "placeholder": _("Apellido Paterno"),
            }),
            'apellido_mat': forms.TextInput(attrs={
                "type": "text",
                "size": "20",
                "placeholder": _("Apellido Materno"),
            }),
            'direccion': forms.TextInput(attrs={
                "type": "text",
                "size": "30",
                "placeholder": _("Direccion, Comuna, Ciudad"),
            }),
            'telefono': forms.TextInput(attrs={
                "type": "text",
                "size": "20",
                "placeholder": _("Telefono"),
            }),
            'email': forms.TextInput(attrs={
                "type": "email",
                "size": "30",
                "placeholder": _("Correo Electronico"),
            })
        }


class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = "__all__"

class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = "__all__"

class JornadaForm(forms.ModelForm):
    class Meta:
        model = Jornada
        fields = "__all__"
        widgets = {
            
            'id_jordana': forms.TextInput(attrs={
                "type": "text",
                "size": "5",
                "placeholder": _("Identtificador"),
            }),
            'codigo': forms.TextInput(attrs={
                "type": "text",
                "size": "4",
                "placeholder": _("JC"),
            }),
            'descripcion': forms.TextInput(attrs={
                "type": "text",
                "size": "25",
                "placeholder": _("Descripcion"),
            }),
            'inicio': forms.TimeInput(attrs={
                "class": "form-control",
                "type" : "time",
                "size": "10",
            }),            
            'termino': forms.TimeInput(attrs={
                "class": "form-control",
                "type" : "time",
                "size": "10",
            }),
        }