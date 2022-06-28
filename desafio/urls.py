from django.urls import path
from .views import una_vista

urlpatterns = [
    path('', una_vista),
]
