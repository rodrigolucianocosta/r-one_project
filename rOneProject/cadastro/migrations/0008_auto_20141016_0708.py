# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0007_auto_20141016_0435'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='Rua',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Nome da Rua'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='endereco',
            name='complemento',
            field=models.CharField(max_length=10, null=True, verbose_name=b'complemento'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='endereco',
            name='endereco',
            field=models.ForeignKey(verbose_name=b'endereco', to='cadastro.Pessoa', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='endereco',
            name='numero',
            field=models.IntegerField(max_length=5, null=True, verbose_name=b'numero'),
            preserve_default=True,
        ),
    ]
