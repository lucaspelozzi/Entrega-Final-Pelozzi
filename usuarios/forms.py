from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class FormularioCreacion(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: '' for k in fields}


class EditarUsuario(UserChangeForm):
    password = None
    email = forms.EmailField(label='eMail: ', max_length=100)
    first_name = forms.CharField(label='Nombre: ', max_length=40)
    last_name = forms.CharField(label='Apellido: ', max_length=40)
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar']