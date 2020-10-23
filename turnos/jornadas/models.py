from django.db import models, connection
from django.utils import timezone


def nombre_foto(instance, filename):
    f, ext = os.path.splitext(filename)
    archivo = '%s%s' % (instance.id_entidad, ext)
    return os.path.join('webcamimages', archivo)


class Entidad(models.Model):
    id_entidad = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=10)
    nombres = models.CharField(max_length=55)
    apellido_pat = models.CharField(max_length=35)
    apellido_mat = models.CharField(max_length=35)
    direccion = models.CharField(max_length=125)
    telefono = models.CharField(max_length=9)
    email = models.CharField(max_length=100)
    foto = models.ImageField(upload_to=nombre_foto, blank=True, null=True)

    @staticmethod
    def registrarent(id_entidad, rut, nombres, apellido_pat, apellido_mat, direccion, telefono, email, foto):
        cur = connection.cursor()
        cur.callproc('registrarent', [id_entidad,
                                      rut, nombres, apellido_pat, apellido_mat, direccion, telefono, email, foto])
        cur.close()

    class Meta:
        managed = True
        db_table = 'entidad'

    def __str__(self):
        return self.nombres

        def __str__(self):
            return self.nombre

        def getNombres(self):
            return self.nombres

        def setNombres(self, nombres):
            self.nombres = nombres

        def getRut(self):
            return self.rut

        def setDni(self, rut):
            self.rut = rut

        def getApellido_Pat(self):
            return self.apellido_pat

        def setApellido_Pat(self, apellido_pat):
            self.apellido_pat = apellido_pat

        def getDireccion(self):
            return self.direccion

        def setDireccion(self, direccion):
            self.direccion = direccion

        def getTelefono(self):
            return self.telefono

        def setTelefono(self, telefono):
            self.telefono = telefono

        def getEmail(self):
            return self.email

        def setEmail(self, email):
            self.email = email


class Jornada(models.Model):
    id_jordana = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=3)
    descripcion = models.CharField(max_length=65)
    inicio = models.TimeField()
    termino = models.TimeField()

    class Meta:
        managed = True
        db_table = 'jornada'

    def __str__(self):
        return self.descripcion


class Turno(models.Model):
    id_turno = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=60)

    class Meta:
        managed = True
        db_table = 'turno'

    def __str__(self):
        return self.descripcion


class Usuario(models.Model):
    user = models.CharField(max_length=60)
    password = models.IntegerField(db_column='pass')
    id_entidad = models.ForeignKey(Entidad, on_delete=models.PROTECT)

    class Meta:
        managed = True
        db_table = 'usuario'


class Asistencia(models.Model):
    id_asistencia = models.AutoField(primary_key=True)
    id_turno = models.ForeignKey(Turno, on_delete=models.PROTECT)
    id_entidad = models.ForeignKey(Entidad, on_delete=models.PROTECT)
    id_jordana = models.ForeignKey(Jornada, on_delete=models.PROTECT)
    ingreso = models.DateTimeField(null=True)
    salida = models.DateTimeField(null=True)
    observacion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'asistencia'
