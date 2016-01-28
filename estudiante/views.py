from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from itertools import islice, chain
from estudiante.models import Taller,Curso,TallerGeneral,Academic_Rank,Limitaciones
from contrato.models import Estudiante
from django.contrib.auth.decorators import login_required
from datetime import date, datetime, timedelta

# Create your views here.
def login_user(request):
    state = "Por favor ingrese a continuacion"
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "Conectado con exito"
                usuario = User.objects.get(username=username)
                fotourl = usuario.estudiante.foto.url
                cedula = usuario.estudiante.cedula
                telefono = usuario.estudiante.telefono
                fecha =date.today()
                programa = usuario.estudiante.programa.nombre_del_programa
                duracion = usuario.estudiante.fecha_de_expiracion
                startdate = date.today()+ timedelta(days=1)
                enddate = startdate + timedelta(days=1)
                nivel  = usuario.estudiante.nivel
                cursos = []
                talleres = []
		latacunga = False
                if Curso.objects.filter(fecha__range=[startdate, enddate]).filter(capacidad_maxima__gt=0).count() > 0 :
                    cursos1 = Curso.objects.filter(fecha__range=[startdate, enddate]).filter(capacidad_maxima__gt=0).\
                        filter(tipo_leccion__in=range(usuario.estudiante.nivel.leccion-10,usuario.estudiante.nivel.leccion+11)).\
                        filter(tipo_nivel=usuario.estudiante.nivel.nivel).filter(sede=usuario.estudiante.sede).exclude(tipo_nivel='xx')
                    cursos2 = Curso.objects.filter(fecha__range=[startdate, enddate]).filter(capacidad_maxima__gt=0).\
                        filter(tipo_nivel='xx').filter(sede=usuario.estudiante.sede)
                    cursos = list(chain(cursos1,cursos2))
                    print cursos
		    latacunga = True
		talleres = Taller.objects.filter(nivel=usuario.estudiante.nivel.nivel).filter(fecha__range=[startdate, enddate]).filter(capacidad__gt=0).filter(lugar=usuario.estudiante.sede)
                talleresg = TallerGeneral.objects.filter(fecha__range=[startdate, enddate]).filter(capacidad__gt=0).filter(lugar=usuario.estudiante.sede)
                print talleres
		latacunga1 = False
		latacunga2 = False
		if talleres.count() > 0:
		    latacunga1 = True
		if talleresg.count() > 0:
		    latacunga2 = True
                # .filter(hora_inicio__gt=time.strftime("%H:%M:%S"))
                return render(request,'contenido.html',{'latacunga':latacunga,'latacunga1':latacunga1,'latacunga2':latacunga2,'username':username,'fecha':fecha,'duracion':duracion,'fotourl':fotourl,'cedula':cedula,'telefono':telefono,'programa':programa,'talleres':talleres,'talleresg':talleresg,'cursos':cursos,'nivel':nivel})
            else:
                state = "Tu cuenta esta desactivada por favor acercarce a oficinas."
        else:
            state = "Usuario o contrasena incorrecta"

    return render(request,'signin.html',{'state':state}, context_instance=RequestContext(request))
@login_required
def cuenta(request):
    state = "Conectado con exito"
    user = request.user.id
    print 'Imprimiendo en usuario'
    print user
    usuario = User.objects.get(id=user)
    print usuario
    fotourl = usuario.estudiante.foto.url
    cedula = usuario.estudiante.cedula
    telefono = usuario.estudiante.telefono
    fecha =date.today()
    programa = usuario.estudiante.programa.nombre_del_programa
    duracion = usuario.estudiante.fecha_de_expiracion
    startdate = date.today()+ timedelta(days=1)
    enddate = startdate + timedelta(days=1)
    nivel  = usuario.estudiante.nivel
    cursos = []
    talleres = []
    latacunga  = False
    if Curso.objects.filter(fecha__range=[startdate, enddate]).filter(capacidad_maxima__gt=0).count() > 0 :
        cursos1 = Curso.objects.filter(fecha__range=[startdate, enddate]).filter(capacidad_maxima__gt=0).\
        filter(tipo_leccion__in=range(usuario.estudiante.nivel.leccion-10,usuario.estudiante.nivel.leccion+11)).\
        filter(tipo_nivel=usuario.estudiante.nivel.nivel).filter(sede=usuario.estudiante.sede)
        cursos2 = Curso.objects.filter(fecha__range=[startdate, enddate]).filter(capacidad_maxima__gt=0).\
                    filter(tipo_nivel='xx').filter(sede=usuario.estudiante.sede)
        cursos = list(chain(cursos1,cursos2))
        print cursos
	latacunga = True
    talleresg = TallerGeneral.objects.filter(fecha__range=[startdate, enddate]).filter(capacidad__gt=0).filter(lugar=usuario.estudiante.sede)
    talleres = Taller.objects.filter(nivel=usuario.estudiante.nivel.nivel).filter(fecha__range=[startdate, enddate]).filter(capacidad__gt=0).filter(lugar=usuario.estudiante.sede)
    print talleres
    latacunga1 = False
    latacunga2 = False
    if talleres.count() > 0:
	latacunga1 = True
    if talleresg.count() > 0:
	latacunga2 = True
        # .filter(hora_inicio__gt=time.strftime("%H:%M:%S"))
    return render(request,'contenido.html',{'latacunga':latacunga,'latacunga1':latacunga1,'latacunga2':latacunga2,'username':request.user,'fecha':fecha,'duracion':duracion,'fotourl':fotourl,'cedula':cedula,'telefono':telefono,'programa':programa,'talleres':talleres,'talleresg':talleresg,'cursos':cursos,'nivel':nivel})

class Busqueda_info_ajax(TemplateView):
    def get(self, request, *args, **kwargs):
        id_taller = request.GET['id']
        print id_taller
        info = Taller.objects.filter(id=id_taller)
        data=serializers.serialize("json", info)
        print data
        return HttpResponse(data, content_type="application/json")

@login_required
def reserva(request):
    estadot = False
    if request.method == 'POST':
        user = request.user.id
        usuario = User.objects.get(id=user)
        fotourl = usuario.estudiante.foto.url
        cedula = usuario.estudiante.cedula
        telefono = usuario.estudiante.telefono
        fecha = date.today()
        programa = usuario.estudiante.programa.nombre_del_programa
        duracion = usuario.estudiante.fecha_de_expiracion
        startdate = date.today()+ timedelta(days=1)
        enddate = startdate + timedelta(days=1)
        nivel  = usuario.estudiante.nivel
        cursos = []
        talleres = []
	latacunga  = False
        taller = request.POST.get('talleres')
        taller_actualizar = Taller.objects.get(pk=taller)
        if Curso.objects.filter(fecha__range=[startdate, enddate]).filter(capacidad_maxima__gt=0).count() > 0 :
            cursos1 = Curso.objects.filter(fecha__range=[startdate, enddate]).filter(capacidad_maxima__gt=0).\
                        filter(tipo_leccion__in=range(usuario.estudiante.nivel.leccion-10,usuario.estudiante.nivel.leccion+11)).\
                        filter(tipo_nivel=usuario.estudiante.nivel.nivel).filter(sede=usuario.estudiante.sede)
            cursos2 = Curso.objects.filter(fecha__range=[startdate, enddate]).filter(capacidad_maxima__gt=0).\
                        filter(tipo_nivel='xx').filter(sede=usuario.estudiante.sede)
            cursos = list(chain(cursos1,cursos2))
            print cursos
	    latacunga = True
        talleres = Taller.objects.filter(nivel=usuario.estudiante.nivel.nivel).filter(fecha__range=[startdate, enddate]).filter(capacidad__gt=0).filter(lugar=usuario.estudiante.sede)
        print talleres
        talleresg = TallerGeneral.objects.filter(fecha__range=[startdate, enddate]).filter(capacidad__gt=0).filter(lugar=usuario.estudiante.sede)
	latacunga1 = False
        latacunga2 = False
        if talleres.count() > 0:
            latacunga1 = True
        if talleresg.count() > 0:
            latacunga2 = True
        if taller_actualizar.estudiantes.all().filter(pk=usuario.estudiante.cedula).count() == 0:
            taller_actualizar.estudiantes.add(usuario.estudiante)
            taller_actualizar.capacidad = taller_actualizar.capacidad - 1
            taller_actualizar.save()
            estadot = True
            return render(request,'contenido.html',{'latacunga':latacunga,'latacunga1':latacunga1,'latacunga2':latacunga2,'username':request.user,'fecha':fecha,'duracion':duracion,'fotourl':fotourl,'cedula':cedula,'telefono':telefono,'programa':programa,'talleres':talleres,'talleresg':talleresg,'cursos':cursos,'nivel':nivel,'estadot':estadot})
        else:
            return render(request,'contenido.html',{'latacunga':latacunga,'latacunga1':latacunga1,'latacunga2':latacunga2,'username':request.user,'fecha':fecha,'duracion':duracion,'fotourl':fotourl,'cedula':cedula,'telefono':telefono,'programa':programa,'talleres':talleres,'talleresg':talleresg,'cursos':cursos,'nivel':nivel,'estadot':estadot})
    else:
        return render(request,'contenido.html',{'latacunga':latacunga,'latacunga1':latacunga1,'latacunga2':latacunga2,'estadot':estadot})


@login_required
def reservar_curso(request):
    estadocurso = False
    if request.method == 'POST':
        user = request.user.id
        usuario = User.objects.get(id=user)
        fotourl = usuario.estudiante.foto.url
        cedula = usuario.estudiante.cedula
        telefono = usuario.estudiante.telefono
        fecha = date.today()
        programa = usuario.estudiante.programa.nombre_del_programa
        duracion = usuario.estudiante.fecha_de_expiracion
        startdate = date.today()+timedelta(days=1)
        enddate = startdate + timedelta(days=1)
        nivel  = usuario.estudiante.nivel
        cursos = []
        talleres = []
	latacunga = False
        curso = request.POST.get('cursos')
        curso_actualizar = Curso.objects.get(pk=curso)
	INICIO = ""
	FIN = ""
	if date.today().weekday() == 0:
	    INICIO = date.today()
	    FIN = date.today() + timedelta(days=6)
	if date.today().weekday() == 1:
	    INICIO = date.today() - timedelta(days=1)
	    FIN = date.today() + timedelta(days=5)
	if date.today().weekday() == 2:
	    INICIO = date.today() - timedelta(days=2)
	    FIN = date.today() + timedelta(days=4)
	if date.today().weekday() == 3:
	    INICIO = date.today() - timedelta(days=3)
	    FIN = date.today() + timedelta(days=3)
	if date.today().weekday() == 4:
	    INICIO = date.today() - timedelta(days=4)
	    FIN = date.today() + timedelta(days=2)
	if date.today().weekday() == 5:
	    INICIO = date.today() - timedelta(days=5)
	    FIN = date.today() + timedelta(days=1)
	if date.today().weekday() == 6:
	    INICIO = date.today() - timedelta(days=6)
	    FIN = date.today()
	valor_limitacion = Limitaciones.objects.filter(fecha_reserva__range=[INICIO,FIN]).filter(estudiante=usuario.estudiante).count() < 3
        if Curso.objects.filter(fecha__range=[startdate, enddate]).filter(capacidad_maxima__gt=0).count() > 0 :
            cursos1 = Curso.objects.filter(fecha__range=[startdate, enddate]).filter(capacidad_maxima__gt=0).\
                        filter(tipo_leccion__in=range(usuario.estudiante.nivel.leccion-10,usuario.estudiante.nivel.leccion+11)).\
                        filter(tipo_nivel=usuario.estudiante.nivel.nivel).filter(sede=usuario.estudiante.sede)
            cursos2 = Curso.objects.filter(fecha__range=[startdate, enddate]).filter(capacidad_maxima__gt=0).\
                        filter(tipo_nivel='xx').filter(sede=usuario.estudiante.sede)
            cursos = list(chain(cursos1,cursos2))
            print cursos
	    latacunga = True
        talleres = Taller.objects.filter(nivel=usuario.estudiante.nivel.nivel).filter(fecha__range=[startdate, enddate]).filter(capacidad__gt=0).filter(lugar=usuario.estudiante.sede)
        talleresg = TallerGeneral.objects.filter(fecha__range=[startdate, enddate]).filter(capacidad__gt=0).filter(lugar=usuario.estudiante.sede)
        print talleres
	latacunga1 = False
	latacunga2 = False
	if talleres.count() > 0:
            latacunga1 = True
        if talleresg.count() > 0:
            latacunga2 = True
	if valor_limitacion:
            if curso_actualizar.tipo_nivel == 'xx' or curso_actualizar.tipo_leccion == 0:
                curso_actualizar.tipo_nivel = usuario.estudiante.nivel.nivel
                curso_actualizar.tipo_leccion = usuario.estudiante.nivel.leccion
                curso_actualizar.save()
	        estadocurso = True
            curso_actualizar = Curso.objects.get(pk=curso)
        if valor_limitacion:
	    if curso_actualizar.tipo_estudiante.count()<= curso_actualizar.max_tipo:
                if curso_actualizar.estudiantes.all().filter(pk=usuario.estudiante.cedula).count() == 0:
                    usuario.estudiante.nivel.leccion = usuario.estudiante.nivel.leccion + 1
                    curso_actualizar.estudiantes.add(usuario.estudiante)
                    curso_actualizar.capacidad_maxima = curso_actualizar.capacidad_maxima - 1
                    curso_actualizar.tipo_estudiante.add(usuario.estudiante.nivel)
                    curso_actualizar.save()
		    usuario.save()               
 		    estadocurso = True
	  	    limitacion = Limitaciones(estudiante=usuario.estudiante, fecha_reserva=date.today())
		    limitacion.save()
                    return render(request,'contenido.html',{'latacunga':latacunga,'latacunga1':latacunga1,'latacunga2':latacunga2,'username':request.user,'fecha':fecha,'duracion':duracion,'fotourl':fotourl,'cedula':cedula,'telefono':telefono,'programa':programa,'talleres':talleres,'talleresg':talleresg,'cursos':cursos,'nivel':nivel,'estadocurso':estadocurso})
                else:
                    return render(request,'contenido.html',{'latacunga':latacunga,'latacunga1':latacunga1,'latacunga2':latacunga2,'username':request.user,'fecha':fecha,'duracion':duracion,'fotourl':fotourl,'cedula':cedula,'telefono':telefono,'programa':programa,'talleres':talleres,'talleresg':talleresg,'cursos':cursos,'nivel':nivel,'estadocurso':estadocurso})
            else:
                return render(request,'contenido.html',{'latacunga':latacunga,'latacunga1':latacunga1,'latacunga2':latacunga2,'username':request.user,'fecha':fecha,'duracion':duracion,'fotourl':fotourl,'cedula':cedula,'telefono':telefono,'programa':programa,'talleres':talleres,'talleresg':talleresg,'cursos':cursos,'nivel':nivel,'estadocurso':estadocurso})
    	else:
            return render(request,'contenido.html',{'latacunga':latacunga,'latacunga1':latacunga1,'latacunga2':latacunga2,'username':request.user,'fecha':fecha,'duracion':duracion,'fotourl':fotourl,'cedula':cedula,'telefono':telefono,'programa':programa,'talleres':talleres,'talleresg':talleresg,'cursos':cursos,'nivel':nivel,'estadocurso':estadocurso})
    else:
        return render(request,'contenido.html',{'latacunga':latacunga,'latacunga1':latacunga1,'latacunga2':latacunga2,'estadocurso':estadocurso})


@login_required
def reservaTaller(request):
    estadoTaller = False
    if request.method == 'POST':
        user = request.user.id
        usuario = User.objects.get(id=user)
        fotourl = usuario.estudiante.foto.url
        cedula = usuario.estudiante.cedula
        telefono = usuario.estudiante.telefono
        fecha = date.today()
        programa = usuario.estudiante.programa.nombre_del_programa
        duracion = usuario.estudiante.fecha_de_expiracion
        startdate = date.today()+ timedelta(days=1)
        enddate = startdate +timedelta(days=1)
        nivel  = usuario.estudiante.nivel
        cursos = []
        talleres = []
	latacunga = False
        taller = request.POST.get('talleresg')
        taller_actualizar = TallerGeneral.objects.get(pk=taller)
        if Curso.objects.filter(fecha__range=[startdate, enddate]).filter(capacidad_maxima__gt=0).count() > 0 :
            cursos1 = Curso.objects.filter(fecha__range=[startdate, enddate]).filter(capacidad_maxima__gt=0).\
                        filter(tipo_leccion__in=range(usuario.estudiante.nivel.leccion-10,usuario.estudiante.nivel.leccion+11)).\
                        filter(tipo_nivel=usuario.estudiante.nivel.nivel).filter(sede=usuario.estudiante.sede)
            cursos2 = Curso.objects.filter(fecha__range=[startdate, enddate]).filter(capacidad_maxima__gt=0).\
                        filter(tipo_nivel='xx').filter(sede=usuario.estudiante.sede)
            cursos = list(chain(cursos1,cursos2))
            print cursos
	    latacunga = True
        talleres = Taller.objects.filter(nivel=usuario.estudiante.nivel.nivel).filter(fecha__range=[startdate, enddate]).filter(capacidad__gt=0).filter(lugar=usuario.estudiante.sede)
        talleresg = TallerGeneral.objects.filter(fecha__range=[startdate, enddate]).filter(capacidad__gt=0).filter(lugar=usuario.estudiante.sede)
        print talleres
	latacunga1 = False
	latacunga2 = False
	if talleres.count() > 0:
            latacunga1 = True
        if talleresg.count() > 0:
            latacunga2 = True
        if taller_actualizar.alumnos.all().filter(pk=usuario.estudiante.cedula).count() == 0:
            taller_actualizar.alumnos.add(usuario.estudiante)
            taller_actualizar.capacidad = taller_actualizar.capacidad - 1
            taller_actualizar.save()
            estadoTaller = True
            return render(request,'contenido.html',{'latacunga':latacunga,'latacunga1':latacunga1,'latacunga2':latacunga2,'username':request.user,'fecha':fecha,'duracion':duracion,'fotourl':fotourl,'cedula':cedula,'telefono':telefono,'programa':programa,'talleres':talleres,'talleresg':talleresg,'cursos':cursos,'nivel':nivel,'estadoTaller':estadoTaller})
        else:
            return render(request,'contenido.html',{'latacunga':latacunga,'latacunga1':latacunga1,'latacunga2':latacunga2,'username':request.user,'fecha':fecha,'duracion':duracion,'fotourl':fotourl,'cedula':cedula,'telefono':telefono,'programa':programa,'talleres':talleres,'talleresg':talleresg,'cursos':cursos,'nivel':nivel,'estadoTaller':estadoTaller})
    else:
        return render(request,'contenido.html',{'latacunga':latacunga,'latacunga1':latacunga1,'latacunga2':latacunga2,'estadoTaller':estadoTaller})



def update(request, pullo):
    if request.method == 'POST':
        user = request.user.id
        taller = Taller.objects.get(pk=pullo)
        print user
        print taller
        return HttpResponseRedirect('/clientes/')
    else:

        return render_to_response('account.html')
@login_required
def academic_rank(request):
    user = request.user.id
    usuario = User.objects.get(id=user)
    estudiante = Estudiante.objects.get(pk=usuario.estudiante.cedula)
    nivel  = usuario.estudiante.nivel
    print estudiante
    academic = []
    academic = Academic_Rank.objects.all().filter(estudiante=estudiante)
    print academic
    fotourl = usuario.estudiante.foto.url
    cedula = usuario.estudiante.cedula
    telefono = usuario.estudiante.telefono
    fecha = date.today()
    programa = usuario.estudiante.programa.nombre_del_programa
    duracion = usuario.estudiante.fecha_de_expiracion
    if academic.count() > 0:

        return  render(request,'rank.html',{'academic':academic,'username':request.user,'duracion':estudiante.fecha_de_expiracion,'fotourl':estudiante.foto.url,'cedula':estudiante.cedula,'telefono':estudiante.telefono,'programa':estudiante.programa,'nivel':nivel})
    else:
        return render(request,'rank.html',{'academic':academic,'username':request.user,'fecha':fecha,'duracion':duracion,'fotourl':fotourl,'cedula':cedula,'telefono':telefono,'programa':programa,'nivel':nivel}, context_instance=RequestContext(request))

