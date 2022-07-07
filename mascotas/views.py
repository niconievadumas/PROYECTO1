from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.base import View
from .models import Gato

class ListadoGatos(ListView):
    model = Gato
    template_name = 'gato/listado_gatos.html'
    
    
class CrearGato(CreateView):
    model = Gato
    template_name = 'gato/crear_gatos.html'
    success_url = 'gatos'
    

class EditarGato(UpdateView):
    model = Gato
    template_name = 'gato/editar_gatos.html'
    success_url = 'gatos'

    

class EliminarGato(DeleteView):
    model = Gato
    template_name = 'gato/eliminar_gatos.html'
    success_url = 'gatos'


# class MostrarGato(View):  
#     model = Gato
#     template_name = 'gato/mostrar_gatos.html'
          