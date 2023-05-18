from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from usuarios.forms import FormularioCreacion, EditarUsuario
from usuarios.models import ModeloUsers


def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            usuario = authenticate(username=nombre_usuario, password=contrasenia)
            django_login(request, usuario)
            return redirect('inicio:inicio')
        else:
            return render(request, 'usuarios/login.html', {'formulario': formulario})
    
    formulario = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'formulario': formulario})


def registro(request):
    
    if request.method == 'POST':
        formulario = FormularioCreacion(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios:login')
        else:
            return render(request, 'usuarios/registro.html', {'formulario': formulario})
    
    formulario = FormularioCreacion()
    return render(request, 'usuarios/registro.html', {'formulario': formulario})


@login_required
def editar_usuario(request):
    
    modelousers, formulado = ModeloUsers.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        formulario = EditarUsuario(request.POST, request.FILES, instance=request.user)
        
        if formulario.is_valid():
            if formulario.cleaned_data.get('avatar_pic'):
                request.user.modelousers.avatar_pic = formulario.cleaned_data.get('avatar_pic')
            request.user.modelousers.save()
            formulario.save()
            return redirect('inicio:inicio')
        else:
            return render(request, 'usuarios/editar_usuario.html', {'formulario': formulario})
    
    formulario = EditarUsuario(initial={'avatar_pic': request.user.modelousers.avatar_pic}, instance=request.user)
    return render(request, 'usuarios/editar_usuario.html', {'formulario': formulario})


class CambioPassword(PasswordChangeView):
    template_name = 'usuarios/cambiar_password.html'
    success_url = reverse_lazy('usuarios:editar_usuario')