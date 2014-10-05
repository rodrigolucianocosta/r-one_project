# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ficha_de_matricula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cid', models.CharField(max_length=100, verbose_name=b'cid')),
                ('nome_do_aluno', models.CharField(max_length=100)),
                ('cartao_sus', models.CharField(max_length=20)),
                ('cpf', models.CharField(max_length=11)),
                ('responsavel_pelo_aluno', models.CharField(max_length=100)),
                ('rua', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('data_de_nascimento', models.DateField()),
                ('naturalidade', models.CharField(max_length=50)),
                ('idade', models.CharField(max_length=2)),
                ('sexo', models.CharField(max_length=1)),
                ('cor', models.CharField(max_length=10)),
                ('nome_do_Pai', models.CharField(max_length=100)),
                ('profissao_do_Pai', models.CharField(max_length=50)),
                ('nome_da_Mae', models.CharField(max_length=100)),
                ('profissao_da_Mae', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=75)),
                ('dia_Atendimento', models.CharField(max_length=100)),
                ('horario_atendimento', models.DateTimeField(verbose_name=b'horario')),
                ('data_matricula', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
