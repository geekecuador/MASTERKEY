# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0003_academic_rank_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='estudiantes',
            field=models.ManyToManyField(to='perfil.Perfil', blank=True),
        ),
    ]
