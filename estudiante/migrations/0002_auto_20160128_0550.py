# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academic_rank',
            name='estudiante',
        ),
        migrations.RemoveField(
            model_name='academic_rank',
            name='nivel',
        ),
    ]
