from datetime import datetime
import defusedxml
from django.db import models


class Empleado(models.Model):
    nombres = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10, unique=True)
    fecha_registro = models.DateField(default=datetime.now)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    edad = models.PositiveIntegerField(default=0)
    salario = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    estado = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='foto/%Y/%m/%d', null=True, blank=True)
    cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True)
    
    def __str__(self):
        return self.nombres
    
    class Meta:
        ordering = ['id']