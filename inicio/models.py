from django.db import models


class Blog(models.Model):
    titulo = models.CharField(max_length=50)
    sub_titulo = models.CharField(max_length=100)
    contenido = models.TextField(max_length=100)
    autor = models.CharField(max_length=50)
    fecha_creacion = models.DateField()
    # imagen
    
    def __str__(self):
        return f"{self.titulo} - {self.sub_titulo}"
    
    
