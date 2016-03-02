# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0004_auto_20160205_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='s_comentarios',
            name='fecha',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='seguimiento_estudiante',
            name='estudiante',
            field=models.ForeignKey(related_name='seguimiento_estudiante', to='contrato.Estudiante'),
        ),
    ]
