from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('registro/', views.registro, name = 'registro'),
    path('editar/', views.editar_usuario, name = 'editar_usuario'),
    path('login/', views.login, name = 'login'),
    path('logout/', LogoutView.as_view(template_name = 'usuarios/logout.html'), name = 'logout'),
    path('cambio-password/', views.CambioPassword.as_view(), name = 'cambiar_password')
]