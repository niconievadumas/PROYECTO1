from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader

from .forms import BusquedaPerro, FormPerro
from .models import Perro
from datetime import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.

def una_vista(request):
    return render(request, 'index.html' )

def crear_perro(request): 

    # nombre =request.POST.get("nombre")
    # edad =request.POST.get("edad") 

    # perro = Perro(nombre=nombre, edad=edad, fecha_creacion=datetime.now())
    # perro.save()

    if request.method == "POST":
        form = FormPerro(request.POST) 

        if form.is_valid():
            data = form.cleaned_data
            fecha = data.get("fecha_creacion")

            perro = Perro(
                nombre=data.get("nombre"), 
                edad=data.get("edad"), 
                fecha_creacion=fecha if fecha else datetime.now()
                )
            perro.save()

            # listado_perros = Perro.objects.all()
            # form = BusquedaPerro()

            # return render(request,"listado_perros.html", {"listado_perros": listado_perros, "form": form})
            return redirect("listado_perros")

        else:
            return render(request, 'perro/crear_perro.html', {"form": form})  
    
    form_perro = FormPerro

    return render(request, 'perro/crear_perro.html', {"form": form_perro})  


# template = loader.get_template('index.html')
    
    # prueba1 = Perro(nombre= 'Nico')
    # prueba2 = Perro(nombre= 'Leo')
    # prueba3 = Perro(nombre= 'Juan')
    # prueba1.save()
    # prueba2.save()
    # prueba3.save()

    # render = template.render({'lista_objetos': [prueba1, prueba2, prueba3]})
    
    # return HttpResponse(render)

def listado_perros(request):

    nombre_de_busqueda = request.GET.get("nombre")

    if nombre_de_busqueda:
        listado_perros = Perro.objects.filter(nombre__icontains=nombre_de_busqueda)   #el __incontains es para poner que lo contenga
    else:
        listado_perros = Perro.objects.all()

        
        
    form = BusquedaPerro()
    return render(request,"perro/listado_perros.html", {"listado_perros": listado_perros, "form": form})

@login_required
def editar_perro(request, id):

    perro = Perro.objects.get(id=id) 

    if request.method == "POST":
        form = FormPerro(request.POST) 

        if form.is_valid():
            perro.nombre = form.cleaned_data.get("nombre")
            perro.edad = form.cleaned_data.get("edad")
            perro.fecha_creacion = form.cleaned_data.get("fecha_creacion")
            perro.save()

            return redirect("listado_perros")

        else:
            return render(request, 'perro/editar_perro.html', {"form": form, "perro":perro})  
    
    form_perro = FormPerro(initial={"nombre": perro.nombre, "edad": perro.edad, "fecha_creacion": perro.fecha_creacion})

    return render(request, 'perro/editar_perro.html', {"form": form_perro, "perro":perro})  

  
    return redirect("listado_perros")
    
@login_required
def eliminar_perro(request, id):

    perro = Perro.objects.get(id=id)
    perro.delete() 

    return redirect("listado_perros")    


def mostrar_perro(request, id):

    perro = Perro.objects.get(id=id)
    
    return render(request, "perro/mostrar_perro.html", {"perro": perro})    
    

