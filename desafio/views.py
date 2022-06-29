from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Perro

# Create your views here.

def una_vista(request):
    return render(request, 'index.html' )

def crear_perro(request):
    
    # template = loader.get_template('index.html')
    
    # prueba1 = Perro(nombre= 'Nico')
    # prueba2 = Perro(nombre= 'Leo')
    # prueba3 = Perro(nombre= 'Juan')
    # prueba1.save()
    # prueba2.save()
    # prueba3.save()

    # render = template.render({'lista_objetos': [prueba1, prueba2, prueba3]})
    
    # return HttpResponse(render)
    
    return render(request, 'mi_template.html', {'lista_objetos': [prueba1, prueba2, prueba3]})   #forma resumida de todo lo anterior

