from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.IntegerField()
    correo = models.EmailField()
    contraseña = models.CharField(max_length=12)
    roles = [
        ('C','Cliente'),
        ('A','Administrador')
    ]
    rol = models.CharField(max_length=5, choices=roles, default='Cliente')

    def __str__(self):
        return self.correo

class Peliculas(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField(max_length=10)
    categoria = models.CharField(max_length=50)

class Salas(models.Model):
    N_sala = models.IntegerField()
    N_asientos = models.IntegerField()