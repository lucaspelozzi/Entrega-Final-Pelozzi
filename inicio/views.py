from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list  import ListView

from inicio.models import Blog

def inicio(request):
    return render(request, 'inicio/inicio.html')

def yo(request):
    return render(request, 'inicio/yo.html')



class BlogListView(ListView):
    model = Blog
    template_name = "inicio/lista_blogs.html"
    

    
class BlogDetailView(DetailView):
    model = Blog
    template_name = "inicio/detelle_blog.html"
    


class BlogCreateView(CreateView):
    model = Blog
    template_name = "inicio/crear_blog.html"
    fields = ['titulo','sub_titulo','contenido','autor','fecha_creacion']
    success_url = '/blogs/'

    
class BlogUpdateView(UpdateView):
    model = Blog
    template_name = "inicio/modificar_blog.html"
    fields = ['titulo','sub_titulo','contenido','autor','fecha_creacion']
    success_url = '/blogs/'
    


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "inicio/eliminar_blog.html"
    success_url = '/blogs/'
    

