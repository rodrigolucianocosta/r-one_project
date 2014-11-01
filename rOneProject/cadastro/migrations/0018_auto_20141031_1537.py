# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0017_remove_atendimentofamiliar_numeromembrosfamiliares'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atendimentofamiliar',
            name='Paciente',
        ),
        migrations.DeleteModel(
            name='AtendimentoFamiliar',
        ),
    ]
