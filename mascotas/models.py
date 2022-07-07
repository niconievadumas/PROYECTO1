from django.db import models

# Create your models here.

class Gato(models.Model):
    apodo = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_creacion = models.DateTimeField(null=True)
 
    def __str__(self):
        return f"Soy un gato llamado Sr. {self.apodo}"     
