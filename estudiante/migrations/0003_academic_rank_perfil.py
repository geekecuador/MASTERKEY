# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_remove_perfil_ape'),
        ('estudiante', '0002_auto_20160128_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='academic_rank',
            name='perfil',
            field=models.ForeignKey(default=None, to='perfil.Perfil'),
            preserve_default=False,
        ),
    ]
