# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cid', models.IntegerField(null=True, verbose_name=b'Cid')),
                ('NomePessoa', models.CharField(max_length=100, null=True, verbose_name=b'Nome')),
                ('Cpf', models.CharField(max_length=14, null=True, verbose_name=b'Cpf')),
                ('Rg', models.CharField(max_length=20, null=True, verbose_name=b'Rg')),
                ('Sexo', models.CharField(max_length=1, null=True, verbose_name=b'Sexo', choices=[(b'M', b'Masculino'), (b'F', b'Feminino')])),
                ('DataNascimento', models.DateField(null=True, verbose_name=b'Data de Nascimento')),
                ('Telefone', models.IntegerField(max_length=15, null=True, verbose_name=b'Telefone')),
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
    ]
