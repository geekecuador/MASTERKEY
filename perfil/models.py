from django.db import models
from contrato.models import Estudiante,Nivel

# Create your models here.

class Perfil(models.Model):
    
    usuario = models.ForeignKey(Estudiante)
    nivel = models.ForeignKey(Nivel)
    def __unicode__(self):
        return (str(self.usuario.encode('utf-8')) +" "+ str(self.nivel.encode('utf-8')))

    
         

         