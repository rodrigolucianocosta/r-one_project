# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NomeCadastro', models.CharField(max_length=100, null=True, verbose_name=b'Nome do Cadastro')),
                ('DataMatricula', models.DateField(null=True, verbose_name=b'Data de Cadastro')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubCadastro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('NomeSubCadastro', models.CharField(max_length=100, verbose_name=b'Nome NomeSubCadastro')),
                ('TipoSubCadastro', models.CharField(max_length=1, verbose_name=b'Tipo SubEvento')),
                ('Cadastro', models.ForeignKey(verbose_name=b'Cadastro', to='cadastro.Cadastros')),
            ],
            options={
                'verbose_name': 'SubCadastro',
                'verbose_name_plural': 'SubCadastros',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='ficha_de_matricula',
        ),
    ]
