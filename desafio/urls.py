from django.urls import path
from .views import una_vista, crear_perro

urlpatterns = [
    path('', una_vista, name="index"),
    path('mi-template/', crear_perro, name= "crear_perro"),
]
