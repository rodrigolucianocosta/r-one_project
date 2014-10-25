# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0011_atendimento_consulta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento',
            name='Consulta',
            field=models.OneToOneField(to='cadastro.Pessoa'),
        ),
    ]
