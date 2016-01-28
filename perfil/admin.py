from django.contrib import admin
from models import Perfil
from estudiante.models import Academic_Rank
from contrato.models import Estudiante,Nivel


class Academic_RankInline(admin.StackedInline):
  model = Academic_Rank
  extra = 1


class PerfilAdmin(admin.ModelAdmin):
  list_display = ('estudiante','nivel',)
  inlines =  [Academic_RankInline,]



  admin.site.register(Perfil,PerfilAdmin)

