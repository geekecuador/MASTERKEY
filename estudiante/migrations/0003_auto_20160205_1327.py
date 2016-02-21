# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0002_auto_20160205_1313'),
    ]

    operations = [
        migrations.CreateModel(
            name='S_comentarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comentario', models.TextField()),
                ('estado', models.ForeignKey(to='estudiante.Estado')),
            ],
        ),
        migrations.RemoveField(
            model_name='seguimientoe',
            name='estudiante',
        ),
        migrations.RemoveField(
            model_name='seguimiento_estudiante',
            name='comentario',
        ),
        migrations.RemoveField(
            model_name='seguimiento_estudiante',
            name='estado',
        ),
        migrations.AlterField(
            model_name='seguimiento_estudiante',
            name='estudiante',
            field=models.ForeignKey(to='contrato.Estudiante'),
        ),
        migrations.DeleteModel(
            name='SeguimientoE',
        ),
        migrations.AddField(
            model_name='s_comentarios',
            name='estudiante',
            field=models.ForeignKey(to='estudiante.Seguimiento_Estudiante'),
        ),
    ]
