from django.db import models
from ckeditor.fields import RichTextField


class Blog(models.Model):
    titulo = models.CharField(max_length=50)
    sub_titulo = models.CharField(max_length=100)
    contenido = RichTextField(max_length=500)
    autor = models.CharField(max_length=50)
    fecha_creacion = models.DateField()
    
    def __str__(self):
        return f"{self.titulo} - {self.sub_titulo}"
    
    
