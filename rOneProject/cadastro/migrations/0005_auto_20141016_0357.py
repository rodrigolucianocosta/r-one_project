# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_auto_20141016_0343'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='DataNascimento',
            field=models.DateField(null=True, verbose_name=b'Data de Nascimento'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='Telefone',
            field=models.IntegerField(null=True, verbose_name=b'Telefone'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='Rg',
            field=models.CharField(max_length=20, null=True, verbose_name=b'Rg'),
        ),
    ]
