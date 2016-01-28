# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('numero_contrato', models.CharField(max_length=8, serialize=False, primary_key=True)),
                ('numero_factura', models.CharField(max_length=10, blank=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.DateField(null=True, verbose_name='Fecha de nacimiento', blank=True)),
                ('cedula', models.CharField(max_length=10, verbose_name='Cedula', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name=b'e-mail', blank=True)),
                ('direccion_domicilio', models.TextField(blank=True)),
                ('telefono', models.CharField(max_length=10, blank=True)),
                ('celular', models.CharField(max_length=10, blank=True)),
                ('empresa', models.CharField(max_length=30, blank=True)),
                ('cargo', models.CharField(max_length=20, blank=True)),
                ('direccion_empresa', models.CharField(max_length=30, blank=True)),
                ('telefono_empresa', models.CharField(max_length=10, blank=True)),
                ('fecha_creacion', models.DateField(verbose_name='Fecha de creacion')),
                ('duracion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('cedula', models.CharField(max_length=11, serialize=False, verbose_name='cedula', primary_key=True)),
                ('foto', models.ImageField(upload_to=b'estudiante')),
                ('nombre', models.CharField(max_length=30, null=True, blank=True)),
                ('apellido', models.CharField(max_length=30, null=True, blank=True)),
                ('contrasena', models.CharField(max_length=35, verbose_name='Contrasena')),
                ('fecha_nacimiento', models.DateField(null=True, verbose_name='fecha de nacimiento', blank=True)),
                ('direccion_domicilio', models.CharField(max_length=25, blank=True)),
                ('telefono', models.CharField(max_length=10, blank=True)),
                ('fecha_de_inicio', models.DateField()),
                ('fecha_de_expiracion', models.DateField()),
                ('lugar_de_trabajo', models.CharField(max_length=30, blank=True)),
                ('contacto_de_emergencia', models.CharField(max_length=30, blank=True)),
                ('relacion_de_contacto_de_emergencia', models.CharField(max_length=30, blank=True)),
                ('telefono_de_contanto_de_emergencia', models.CharField(max_length=10, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nivel', models.CharField(max_length=2)),
                ('leccion', models.IntegerField()),
                ('tema', models.CharField(max_length=35, verbose_name='Actividad')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cedula', models.CharField(max_length=10, verbose_name='Cedula')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('horario_lunes_inicio_manana', models.TimeField(null=True, blank=True)),
                ('horario_lunes_fin_manana', models.TimeField(null=True, blank=True)),
                ('horario_lunes_inicio_tarde', models.TimeField(null=True, blank=True)),
                ('horario_lunes_fin_tarde', models.TimeField(null=True, blank=True)),
                ('horario_martes_inicio_manana', models.TimeField(null=True, blank=True)),
                ('horario_martes_fin_manana', models.TimeField(null=True, blank=True)),
                ('horario_martes_inicio_tarde', models.TimeField(null=True, blank=True)),
                ('horario_martes_fin_tarde', models.TimeField(null=True, blank=True)),
                ('horario_miercoles_inicio_manana', models.TimeField(null=True, blank=True)),
                ('horario_miercoles_fin_manana', models.TimeField(null=True, blank=True)),
                ('horario_miercoles_inicio_tarde', models.TimeField(null=True, blank=True)),
                ('horario_miercoles_fin_tarde', models.TimeField(null=True, blank=True)),
                ('horario_jueves_inicio_manana', models.TimeField(null=True, blank=True)),
                ('horario_jueves_fin_manana', models.TimeField(null=True, blank=True)),
                ('horario_jueves_inicio_tarde', models.TimeField(null=True, blank=True)),
                ('horario_jueves_fin_tarde', models.TimeField(null=True, blank=True)),
                ('horario_viernes_inicio_manana', models.TimeField(null=True, blank=True)),
                ('horario_viernes_fin_manana', models.TimeField(null=True, blank=True)),
                ('horario_viernes_inicio_tarde', models.TimeField(null=True, blank=True)),
                ('horario_viernes_fin_tarde', models.TimeField(null=True, blank=True)),
                ('horario_sabado_inicio_manana', models.TimeField(null=True, blank=True)),
                ('horario_sabado_fin_manana', models.TimeField(null=True, blank=True)),
                ('horario_sabado_inicio_tarde', models.TimeField(null=True, blank=True)),
                ('horario_sabado_fin_tarde', models.TimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('nombre_del_programa', models.CharField(max_length=25, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('nombre_sede', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('direccion', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=20)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('ciudad', models.ForeignKey(to='contrato.Ciudad')),
            ],
        ),
        migrations.AddField(
            model_name='profesor',
            name='sede',
            field=models.ForeignKey(to='contrato.Sede'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='nivel',
            field=models.ForeignKey(to='contrato.Nivel'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='programa',
            field=models.ForeignKey(to='contrato.Programa'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='sede',
            field=models.ForeignKey(to='contrato.Sede'),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='usuario',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contrato',
            name='beneficiarios',
            field=models.ManyToManyField(to='contrato.Estudiante'),
        ),
        migrations.AddField(
            model_name='contrato',
            name='sede_firma_contrato',
            field=models.ForeignKey(to='contrato.Sede'),
        ),
    ]
