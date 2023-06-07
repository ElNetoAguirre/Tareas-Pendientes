"""
models.py "base"
"""
from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
    """Clase Tarea"""
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    completo = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Función"""
        return self.titulo

    class Meta:
        """Clase Meta"""
        ordering = ["completo"]
