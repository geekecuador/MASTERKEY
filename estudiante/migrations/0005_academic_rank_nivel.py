# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0001_initial'),
        ('estudiante', '0004_auto_20160128_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='academic_rank',
            name='nivel',
            field=models.ForeignKey(default=None, to='contrato.Nivel'),
            preserve_default=False,
        ),
    ]
