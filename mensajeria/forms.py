from django import forms
from django.contrib.auth.models import User

class MensajeForm(forms.Form):
    destinatario = forms.ModelChoiceField(queryset=User.objects.all())
    contenido = forms.CharField(widget=forms.Textarea)