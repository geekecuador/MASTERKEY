# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0001_initial'),
        ('estudiante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seguimiento_Estudiante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comentario', models.TextField()),
                ('estado', models.ForeignKey(to='estudiante.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='SeguimientoE',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estudiante', models.ForeignKey(to='contrato.Estudiante')),
            ],
        ),
        migrations.AddField(
            model_name='seguimiento_estudiante',
            name='estudiante',
            field=models.ForeignKey(to='estudiante.SeguimientoE'),
        ),
    ]
