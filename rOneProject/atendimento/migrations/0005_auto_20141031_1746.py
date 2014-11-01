# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0004_auto_20141031_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atendimento',
            name='LocalEvento',
        ),
        migrations.AddField(
            model_name='atendimento',
            name='ResponsavelMarcacao',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Responsavel pela Marcacao'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='SalaAtendimento',
            field=models.IntegerField(max_length=2, null=True, verbose_name=b'Sala de Atendimento'),
        ),
        migrations.AlterField(
            model_name='atendimento',
            name='TipoAtendimento',
            field=models.CharField(max_length=1, null=True, verbose_name=b'Tipo de Atendimento', choices=[(b'A', b'RETORNO'), (b'B', b'CONSULTA'), (b'C', b'AGENDAMENTO')]),
        ),
        migrations.AlterField(
            model_name='atendimentofamiliar',
            name='AtendimentoF',
            field=models.ForeignKey(verbose_name=b'Atendimento Familiar', to='atendimento.Atendimento'),
        ),
        migrations.AlterField(
            model_name='atendimentofamiliar',
            name='TipoAtendimento',
            field=models.CharField(max_length=1, null=True, verbose_name=b'Tipo SubEvento', choices=[(b'A', b'RETORNO'), (b'B', b'CONSULTA'), (b'C', b'AGENDAMENTO')]),
        ),
    ]
