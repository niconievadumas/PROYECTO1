from django.urls import path
from .views import una_vista, crear_perro, listado_perros, eliminar_perro, editar_perro, mostrar_perro

urlpatterns = [
    path('', una_vista, name="index"),
    path('crear-perro/', crear_perro, name= "crear_perro"),
    path('perros/', listado_perros, name= "listado_perros"),
    path('editar-perro/<int:id>/', editar_perro, name= "editar_perro"),
    path('eliminar-perro/<int:id>/', eliminar_perro, name= "eliminar_perro"),
    path('mostrar-perro/<int:id>/', mostrar_perro, name= "mostrar_perro")
]
 