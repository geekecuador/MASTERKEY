# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_remove_perfil_ape'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='id',
        ),
        migrations.AddField(
            model_name='perfil',
            name='cedula',
            field=models.CharField(default=None, max_length=11, serialize=False, verbose_name='cedula', primary_key=True),
            preserve_default=False,
        ),
    ]
