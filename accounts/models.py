from django.db import models
from django.contrib.auth.models import User

class MasDatosUsuario(models.Model):
    # user  = models.ForeignKey(User, on_delete=models.CASCADE) #el cascade es para cuando se elimina el usuario princ
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    