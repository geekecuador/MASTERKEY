from django.db import models
from contrato.models import Estudiante,Nivel
# Create your models here.

class Perfil(models.Model):

    estudiante = models.ForeignKey(Estudiante)
    nivel = models.ForeignKey(Nivel)
    def __str__(self):
        return  (str(self.nombre.encode('utf-8')) +" "+ str(self.nivel.nivel)+" "+ str(self.nivel.leccion)) 
