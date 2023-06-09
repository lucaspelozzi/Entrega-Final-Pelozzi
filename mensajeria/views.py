from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect

from mensajeria.models import Mensaje
from mensajeria.forms import MensajeForm

@method_decorator(login_required, name='dispatch')
class EnviarMensaje(LoginRequiredMixin, View):
    template_name = 'mensajeria/enviar_mensaje.html'
    form_class = MensajeForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            remitente = request.user
            destinatario_id = form.cleaned_data['destinatario'].id
            destinatario = User.objects.get(id=destinatario_id)
            contenido = form.cleaned_data['contenido']

            mensaje = Mensaje(sender=remitente, recipient=destinatario, content=contenido)
            mensaje.save()

            return redirect('mensajeria:mensajes_enviados')

        return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class MensajesRecibidos(LoginRequiredMixin, View):
    template_name = 'mensajeria/mensajes_recibidos.html'

    def get(self, request):
        usuario = request.user
        mensajes = Mensaje.objects.filter(recipient=usuario)

        return render(request, self.template_name, {'mensajes': mensajes})


@method_decorator(login_required, name='dispatch')
class MensajesEnviados(LoginRequiredMixin, View):
    template_name = 'mensajeria/mensajes_enviados.html'

    def get(self, request):
        usuario = request.user
        mensajes = Mensaje.objects.filter(sender=usuario)

        return render(request, self.template_name, {'mensajes': mensajes})
