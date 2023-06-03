from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy

from usuarios.models import ModeloUsers
from usuarios.forms import FormularioCreacion, EditarUsuario


def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            user = authenticate(username=nombre_usuario, password=contrasenia)
            django_login(request, user)
            ModeloUsers.objects.get_or_create(user=user)
            return redirect('inicio:inicio')
        else:
            return render(request, 'usuarios/login.html', {'form': formulario})
    
    formulario = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': formulario})


def registro(request):
    
    if request.method == 'POST':
        formulario = FormularioCreacion(request.POST)
        
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios:login')
        else:
            return render(request, 'usuarios/registro.html', {'form': formulario})
    
    formulario = FormularioCreacion()
    return render(request, 'usuarios/registro.html', {'form': formulario})


@login_required
def editar_usuario(request):
    
    modelousers, creado = ModeloUsers.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        formulario = EditarUsuario(request.POST, request.FILES, instance=request.user)
        
        if formulario.is_valid():
            if formulario.cleaned_data.get('avatar'):
                request.user.modelousers.avatar = formulario.cleaned_data.get('avatar')
                request.user.modelousers.save()
            formulario.save()
            return redirect('usuarios:editar_usuario')
        else:
            return render(request, 'usuarios/editar_usuario.html', {'form': formulario})
    
    formulario = EditarUsuario(initial={'avatar': request.user.modelousers.avatar}, instance=request.user)
    return render(request, 'usuarios/editar_usuario.html', {'form': formulario})


class CambioPassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/cambiar_password.html'
    success_url = reverse_lazy('usuarios:editar_usuario')