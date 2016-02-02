from django.contrib import admin
from models import Taller,Curso,Seguimiento,Estado,TallerGeneral,Academic_Rank,Limitaciones
# Register your models here.


class TallerAdmin(admin.ModelAdmin):
	list_display = ('tema','fecha','hora_inicio','hora_fin','capacidad','profesor','lugar','nivel',)
	#filter_horizontal = ('alumnos',)

class TallerGAdmin(admin.ModelAdmin):
   	list_display = ('tema','fecha','hora_inicio','hora_fin','capacidad','profesor','lugar',)
        #filter_horizontal = ('alumnos',)

class CursoAdmin(admin.ModelAdmin):
 	list_display = ('fecha','hora_inicio','hora_fin','capacidad_maxima','sede','profesor','tipo_nivel','tipo_leccion','max_tipo',)
 	list_editable = ('profesor',)
 	list_filter = ('sede','fecha','hora_inicio',)
 	filter_horizontal = ('estudiantes','tipo_estudiante',)


class SeguimientoAdmin(admin.ModelAdmin):
 	list_display = ('estudiante','comentario','estado',)
 	list_filter = ('estado',)
 	list_editable = ('estado',)
 	raw_id_fields = ('estudiante',)

class Academic_RankAdmin(admin.ModelAdmin):
 	list_display = ('estudiante','nivel','fecha','hora','nota','comentarios','firma_alumno','profesor',)
 	raw_id_fields = ('nivel',)

admin.site.register(Academic_Rank,Academic_RankAdmin)
admin.site.register(Taller,TallerAdmin)
admin.site.register(TallerGeneral,TallerGAdmin)
admin.site.register(Curso,CursoAdmin)
admin.site.register(Seguimiento,SeguimientoAdmin)
admin.site.register(Estado)
admin.site.register(Limitaciones)

