# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0006_auto_20141031_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CodigoPrincipal', models.CharField(max_length=10, null=True, verbose_name=b'Codigo do Cid')),
                ('SubCodigo', models.CharField(max_length=2, null=True, verbose_name=b'SubCodigo do Cid', blank=True)),
                ('ciddescricao', models.CharField(max_length=100, null=True, verbose_name=b'descriacao do cid')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NomePessoa', models.CharField(max_length=100, null=True, verbose_name=b'Nome')),
                ('Cpf', models.CharField(max_length=11, null=True, verbose_name=b'Cpf')),
                ('Rg', models.CharField(max_length=20, null=True, verbose_name=b'Rg')),
                ('Sexo', models.CharField(max_length=1, null=True, verbose_name=b'Sexo', choices=[(b'M', b'Masculino'), (b'F', b'Feminino')])),
                ('Etinia', models.CharField(max_length=10, null=True, verbose_name=b'Etinia')),
                ('NascimentoData', models.DateField(null=True, verbose_name=b'Data de Nascimento')),
                ('Telefone', models.IntegerField(max_length=10, null=True, verbose_name=b'Telefone')),
                ('Celular', models.IntegerField(max_length=10, unique=True, null=True)),
                ('NomeMae', models.CharField(max_length=50, null=True, verbose_name=b'Nome da Mae')),
                ('NomePai', models.CharField(max_length=50, null=True, verbose_name=b'Nome do Pai')),
                ('Rua', models.CharField(max_length=100, null=True, verbose_name=b'Nome da Rua')),
                ('numero', models.IntegerField(max_length=5, null=True, verbose_name=b'numero')),
                ('complemento', models.CharField(max_length=10, null=True, verbose_name=b'complemento')),
                ('bairro', models.CharField(max_length=100, null=True, verbose_name=b'Bairro')),
                ('cidade', models.CharField(max_length=100, null=True, verbose_name=b'Cidade')),
                ('uf', models.CharField(max_length=2, null=True, verbose_name=b'UF', choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amap\xe1'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Cear\xe1'), ('DF', 'Distrito Federal'), ('ES', 'Esp\xedrito Santo'), ('GO', 'Goi\xe1s'), ('MA', 'Maranh\xe3o'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Par\xe1'), ('PB', 'Para\xedba'), ('PR', 'Paran\xe1'), ('PE', 'Pernambuco'), ('PI', 'Piau\xed'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rond\xf4nia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'S\xe3o Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('pessoa_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='atendimento.Pessoa')),
                ('CartaoSus', models.CharField(max_length=20, null=True, verbose_name=b'Cartao Sus')),
            ],
            options={
            },
            bases=('atendimento.pessoa',),
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('pessoa_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='atendimento.Pessoa')),
                ('Crm', models.CharField(max_length=10, null=True, verbose_name=b'Crm')),
                ('Especialidade', models.CharField(max_length=20, null=True, verbose_name=b'Especialidade')),
            ],
            options={
            },
            bases=('atendimento.pessoa',),
        ),
        migrations.RemoveField(
            model_name='atendimentofamiliar',
            name='AtendimentoF',
        ),
        migrations.RemoveField(
            model_name='atendimentofamiliar',
            name='AtendimentoFamiliar',
        ),
        migrations.RemoveField(
            model_name='atendimentofamiliar',
            name='DataSubEvento',
        ),
        migrations.RemoveField(
            model_name='atendimentofamiliar',
            name='DuracaoSubEvento',
        ),
        migrations.RemoveField(
            model_name='atendimentofamiliar',
            name='LocalSubEvento',
        ),
        migrations.RemoveField(
            model_name='atendimentofamiliar',
            name='NumParticipantesSubEvento',
        ),
    ]
