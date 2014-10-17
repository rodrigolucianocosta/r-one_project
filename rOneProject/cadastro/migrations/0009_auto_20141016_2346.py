# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0008_auto_20141016_0708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='endereco',
            name='endereco',
        ),
        migrations.DeleteModel(
            name='Endereco',
        ),
        migrations.AddField(
            model_name='pessoa',
            name='Rua',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Nome da Rua'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='Sexo',
            field=models.CharField(max_length=1, null=True, verbose_name=b'Sexo', choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amap\xe1'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Cear\xe1'), ('DF', 'Distrito Federal'), ('ES', 'Esp\xedrito Santo'), ('GO', 'Goi\xe1s'), ('MA', 'Maranh\xe3o'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Par\xe1'), ('PB', 'Para\xedba'), ('PR', 'Paran\xe1'), ('PE', 'Pernambuco'), ('PI', 'Piau\xed'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rond\xf4nia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'S\xe3o Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='bairro',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Bairro'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='cidade',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Cidade'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='complemento',
            field=models.CharField(max_length=10, null=True, verbose_name=b'complemento'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='numero',
            field=models.IntegerField(max_length=5, null=True, verbose_name=b'numero'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='uf',
            field=models.CharField(max_length=2, null=True, verbose_name=b'UF', choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amap\xe1'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Cear\xe1'), ('DF', 'Distrito Federal'), ('ES', 'Esp\xedrito Santo'), ('GO', 'Goi\xe1s'), ('MA', 'Maranh\xe3o'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Par\xe1'), ('PB', 'Para\xedba'), ('PR', 'Paran\xe1'), ('PE', 'Pernambuco'), ('PI', 'Piau\xed'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rond\xf4nia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'S\xe3o Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='Celular',
            field=models.IntegerField(max_length=10, unique=True, null=True),
        ),
    ]
