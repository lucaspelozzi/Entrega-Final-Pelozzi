from django.urls import path

from mensajeria.views import EnviarMensaje, MensajesRecibidos, MensajesEnviados

app_name = 'mensajeria'

urlpatterns = [
    path('enviar-mensaje/', EnviarMensaje.as_view(template_name='mensajeria/enviar_mensaje.html'), name='enviar_mensaje'),
    path('mensajes-recibidos/', MensajesRecibidos.as_view(template_name='mensajeria/mensajes_recibidos.html'), name='mensajes_recibidos'),
    path('mensajes-enviados/', MensajesEnviados.as_view(template_name='mensajeria/mensajes_enviados.html'), name='mensajes_enviados'),
]