from django.db import models

# Create your models here.
class Agenda(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    servicio = models.CharField(max_length=200)
    mensaje = models.TextField(blank=True)
    origen = models.CharField(max_length=50, default='index')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.servicio}"