from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from datetime import timedelta, date
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.db.models import Count, Sum, Max
from .models import *
from .forms import *


def Panel(request):
    return render(request, "panel.html")

# Guardar imagen


class Captura(TemplateView):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        self.filename = self.kwargs['cedula']+'.jpg'
        return super(Captura, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):    # save it somewhere
        f = open(settings.MEDIA_ROOT + '/webcamimages/' + self.filename, 'wb')
        f.write(request.body)
        f.close()
        # return the URL
        return HttpResponse("/media/webcamimages/" + self.filename)

    def get(self, request, *args, **kwargs):
        return HttpResponse('No esta pasando el POST')

# CRUD Entidades - Empleados


def Empleados(request):
    entidad = Entidad.objects.all()
    return render(request, "jornada_empleados.html", {'object_list': entidad, 'tipo_objeto': "entidad"})


def RegistrarEntidad(request):
    if request.method == 'POST':
        form = EntidadForm(request.POST)
        if form.is_valid():
            ne = form.save(commit=False)
            if len(ne.rut) > 9:
                try:
                    Entidad.registrarent(ne.id_entidad, ne.rut, ne.nombres, ne.apellido_pat,
                                         ne.apellido_mat, ne.direccion, ne.telefono, ne.email, ne.foto)
                    form = EntidadForm()
                    return render(request, 'registrarEntidad.html', {'form': form, 'mjsexitoso': "puede ingresar mas Empleados"})
                except ValueError:
                    form = EntidadForm()
                    return render(request, 'registrarEntidad.html', {'form': form, 'error': "ocurrio un problema al intentar registrar"})
            else:
                form = EntidadForm()
                return render(request, 'registrarEntidad.html', {'form': form, 'error': "contenido del formulario incorrecto"})
        else:
            form = EntidadForm()
            return render(request, 'registrarEntidad.html', {'form': form, 'error': "recorcholis"})
    else:
        form = EntidadForm()
        return render(request, 'registrarEntidad.html', {'form': form, 'error': "OOps"})


def form_valid(self, form):
    form.instance.foto = 'webcamimages/' + form.instance.id_entidad + ".jpg"
    return super(RegistrarEntidad, self).form_valid(form)


def Empleados_editar(request, item):
    entidad = get_object_or_404(Entidad, pk=item)
    form = EntidadForm(request.POST or None, instance=entidad)
    if form.is_valid():
        form.save()
        return redirect('jornadas:empleados')
    return render(request, 'actualizar.html', {'form': form, 'tipo_objeto': "entidad"})

# Asistencia


def AsistenciaLista(request):
    asistencia = Asistencia.objects.all()
    return render(request, "list_asistencia.html", {'object_list': asistencia, 'tipo_objeto': "asistencia"})


def EliminarAsistencia(request, item):
    asistencias = get_object_or_404(Asistencia, pk=item)
    asistencia = Asistencia.objects.all()
    if request.method == 'POST':
        asistencia.delete()
        return redirect('asistencias')
    return render(request, 'list_asistencia.html', {'object_list': asistencia, 'object': asistencias, 'eliminar': 'True', 'tipo_objeto': "asistencia"})


def AsistenciaEditar(request, item):
    asistencias = get_object_or_404(Asistencia, pk=item)
    form = AsistenciaForm(request.POST or None, instance=asistencias)
    if form.is_valid():
        form.save()
        return redirect('editasistencia')
    return render(request, 'actualizar.html', {'form': form, 'tipo_objeto': "asistencias"})


def TurnoLista(request):
    turno = Turno.objects.all()
    return render(request, "list_turnos.html", {'object_list': turno, 'tipo_objeto': "turno"})

def EditaTurno(request, item):
    turnos = get_object_or_404(Turno, pk=item)
    form = TurnoForm(request.POST or None, instance=turnos)
    if form.is_valid():
        form.save()
        return redirect('editaturno')
    return render(request, 'actualizar.html', {'form': form, 'tipo_objeto': "turnos"})


def EliminaTurno(request, item):
    turnos = get_object_or_404(Turno, pk=item)
    turno = Turno.objects.all()
    if request.method == 'POST':
        turno.delete()
        return redirect('turnos')
    return render(request, 'list_turnos.html', {'object_list': turno, 'object': turnos, 'eliminar': 'True', 'tipo_objeto': "turno"})