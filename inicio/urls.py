from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name = 'inicio'),
    path('yo', views.yo, name = 'yo'),
    path('blogs/', views.BlogListView.as_view(), name = 'lista_blogs'),
    path('blog/crear/', views.BlogCreateView.as_view(), name = 'crear_blog'),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name = 'detalle_blog'),
    path('blog/<int:pk>/modificar/', views.BlogUpdateView.as_view(), name = 'modificar_blog'),
    path('blog/<int:pk>/eliminar/', views.BlogDeleteView.as_view(), name = 'eliminar_blog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
