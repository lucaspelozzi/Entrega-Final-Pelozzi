from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from PIL import Image

class Blog(models.Model): 
    titulo = models.CharField(max_length=50)
    sub_titulo = models.CharField(max_length=100)
    contenido = RichTextField(max_length=500)
    autor = models.CharField(max_length=50)
    fecha_creacion = models.DateField()
    imagen = models.ImageField(upload_to='imagenes', null=True)

    def __str__(self):
        return f"{self.titulo} - {self.sub_titulo}"
    
    def imagen_url(self):
        if self.imagen and hasattr(self.imagen, 'url'):
            return self.imagen.url
        return ''

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.imagen:
            img = Image.open(self.imagen.path)

            if img.height > 500 or img.width > 500:
                output_size = (500, 500)
                img.thumbnail(output_size)
                img.save(self.imagen.path)