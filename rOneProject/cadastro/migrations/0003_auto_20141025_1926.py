# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_atendimento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atendimento',
            old_name='Consulta',
            new_name='Paciente',
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='Cpf',
            field=models.CharField(max_length=11, null=True, verbose_name=b'Cpf'),
        ),
    ]
