# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0013_auto_20141029_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atendimentofamiliar',
            name='ComposicaoFamiliar1',
        ),
        migrations.RemoveField(
            model_name='atendimentofamiliar',
            name='ComposicaoFamiliar2',
        ),
        migrations.RemoveField(
            model_name='atendimentofamiliar',
            name='ComposicaoFamiliar3',
        ),
        migrations.RemoveField(
            model_name='atendimentofamiliar',
            name='ComposicaoFamiliar4',
        ),
        migrations.RemoveField(
            model_name='atendimentofamiliar',
            name='ComposicaoFamiliar5',
        ),
    ]
