# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NomeAtendimento', models.CharField(max_length=100, null=True, verbose_name=b'Nome do Evento')),
                ('TipoAtendimento', models.CharField(max_length=1, null=True, verbose_name=b'Tipo de Evento', choices=[(b'A', b'RETORNO'), (b'B', b'CONSULTA')])),
                ('DataAtendimento', models.DateField(null=True, verbose_name=b'Data de Atendimento')),
                ('LocalEvento', models.CharField(max_length=100, null=True, verbose_name=b'Local do Evento')),
            ],
            options={
                'verbose_name': 'Atendimento',
                'verbose_name_plural': 'Atendimentos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AtendimentoFamiliar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('AtendimentoFamiliar', models.CharField(max_length=100, null=True, verbose_name=b'Atendimento Familiar')),
                ('TipoAtendimento', models.CharField(max_length=1, null=True, verbose_name=b'Tipo SubEvento', choices=[(b'A', b'RETORNO'), (b'B', b'CONSULTA')])),
                ('DataSubEvento', models.DateField(null=True, verbose_name=b'Data SubEvento')),
                ('DuracaoSubEvento', models.IntegerField(help_text=b'Informar dura\xc3\xa7\xc3\xa3o em minutos', null=True, verbose_name=b'Duracao SubEvento')),
                ('LocalSubEvento', models.CharField(max_length=100, null=True, verbose_name=b'Local Subevento')),
                ('NumParticipantesSubEvento', models.IntegerField(null=True, verbose_name=b'Numero de Participantes SubEvento', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)])),
                ('InicioInscricao', models.DateField(null=True, verbose_name=b'Data inicio da inscri\xc3\xa7ao')),
                ('FimInscricao', models.DateField(null=True, verbose_name=b'Data Fim da inscricao')),
                ('AtendimentoF', models.ForeignKey(verbose_name=b'Evento', to='atendimento.Atendimento')),
            ],
            options={
                'verbose_name': 'Atendimento Familiar',
                'verbose_name_plural': 'AtendimentoFamiliar',
            },
            bases=(models.Model,),
        ),
    ]
