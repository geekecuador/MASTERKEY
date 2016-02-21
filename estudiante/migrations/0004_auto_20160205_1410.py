# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0003_auto_20160205_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seguimiento_estudiante',
            name='estudiante',
            field=models.ForeignKey(related_name='seguimiento_sstudiante', to='contrato.Estudiante'),
        ),
    ]
