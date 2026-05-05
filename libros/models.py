from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    cantidad_disponible = models.IntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-fecha_creacion']
