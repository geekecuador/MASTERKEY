# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Academic_Rank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('nota', models.CharField(default=b'Good', max_length=15, choices=[(b'Excellent', b'Excellent'), (b'Very Good', b'Very Good'), (b'Good', b'Good'), (b'Work at home', b'Work at home'), (b'Repeat', b'Repeat'), (b'Continue', b'Continue')])),
                ('comentarios', models.CharField(max_length=35, blank=True)),
                ('firma_alumno', models.BooleanField()),
                ('estudiante', models.ForeignKey(to='contrato.Estudiante')),
                ('nivel', models.ForeignKey(to='contrato.Nivel')),
                ('profesor', models.ForeignKey(to='contrato.Profesor')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('capacidad_maxima', models.PositiveSmallIntegerField(default=6)),
                ('tipo_nivel', models.CharField(default=b'xx', max_length=b'2')),
                ('tipo_leccion', models.PositiveSmallIntegerField(default=0)),
                ('max_tipo', models.PositiveSmallIntegerField(default=3)),
                ('estudiantes', models.ManyToManyField(to='contrato.Estudiante', blank=True)),
                ('profesor', models.ForeignKey(to='contrato.Profesor')),
                ('sede', models.ForeignKey(to='contrato.Sede')),
                ('tipo_estudiante', models.ManyToManyField(related_name='tipo_estudiante', to='contrato.Nivel', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Limitaciones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_reserva', models.DateField()),
                ('estudiante', models.ForeignKey(to='contrato.Estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comentario', models.TextField()),
                ('estado', models.ForeignKey(to='estudiante.Estado')),
                ('estudiante', models.ForeignKey(to='contrato.Estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Taller',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tema', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('capacidad', models.IntegerField()),
                ('nivel', models.CharField(max_length=2)),
                ('estudiantes', models.ManyToManyField(related_name='alumnos', to='contrato.Estudiante', blank=True)),
                ('lugar', models.ForeignKey(to='contrato.Sede')),
                ('profesor', models.ForeignKey(to='contrato.Profesor')),
            ],
        ),
        migrations.CreateModel(
            name='TallerGeneral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tema', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('capacidad', models.IntegerField()),
                ('alumnos', models.ManyToManyField(to='contrato.Estudiante', blank=True)),
                ('lugar', models.ForeignKey(to='contrato.Sede')),
                ('profesor', models.ForeignKey(to='contrato.Profesor')),
            ],
        ),
    ]
