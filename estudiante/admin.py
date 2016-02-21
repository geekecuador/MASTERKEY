from django.contrib import admin
from models import Taller,Curso,Seguimiento,Estado,TallerGeneral,Academic_Rank,Limitaciones,S_comentarios,Seguimiento_Estudiante
# from actions import export_as_excel
# from actions import export_as_json
# from actions import export_selected_objects
from actions import export_as_csv_action

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
 	#actions = (export_as_excel,export_as_json,export_selected_objects)
 	actions = [export_as_csv_action("Exportar a Ecxel", fields=['fecha','hora_inicio','hora_fin','capacidad_maxima','sede','profesor','tipo_nivel','tipo_leccion','max_tipo',])]



class SeguimientoAdmin(admin.ModelAdmin):
 	list_display = ('estudiante','comentario','estado',)
 	list_filter = ('estado',)
 	list_editable = ('estado',)
 	raw_id_fields = ('estudiante',)

class Academic_RankAdmin(admin.ModelAdmin):
 	list_display = ('estudiante','nivel','fecha','hora','nota','comentarios','firma_alumno','profesor',)
 	raw_id_fields = ('nivel',)
 	#date_hierarchy = ('publish_date',)

class S_comentariosAdmin(admin.ModelAdmin):
	list_display =('estudiante','comentario','estado',)


class S_comentariosInline(admin.TabularInline):
  model = S_comentarios
  extra = 1

class Seguimiento_EstudianteAdmin(admin.ModelAdmin):
	list_display =('estudiante',)
	inlines =  [S_comentariosInline,]




admin.site.register(Academic_Rank,Academic_RankAdmin)
admin.site.register(Taller,TallerAdmin)
admin.site.register(TallerGeneral,TallerGAdmin)
admin.site.register(Curso,CursoAdmin)
admin.site.register(Seguimiento,SeguimientoAdmin)
admin.site.register(Estado)
admin.site.register(Limitaciones)
admin.site.register(S_comentarios,S_comentariosAdmin)
admin.site.register(Seguimiento_Estudiante,Seguimiento_EstudianteAdmin)


