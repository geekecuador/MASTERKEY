from django.contrib import admin
from models import Perfil
from estudiante.models import Academic_Rank


class Academic_RankInline(admin.StackedInline):
  		model = Academic_Rank
  		extra = 1
  		


class PerfilAdmin(admin.ModelAdmin):

  		list_display = ('usuario','nivel')
  		raw_id_fields = ('usuario',)
  		search_fields = ('usuario',)
  		inlines =  [Academic_RankInline,]

  		
  


admin.site.register(Perfil,PerfilAdmin)