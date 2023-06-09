from django import forms
from inicio.models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['titulo', 'sub_titulo', 'contenido', 'autor', 'fecha_creacion', 'imagen']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].widget.attrs.update({'class': 'form-control-file'})