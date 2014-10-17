# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0005_auto_20141016_0357'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='Celular',
            field=models.IntegerField(max_length=10, unique=True, null=True, validators=[django.core.validators.RegexValidator(regex=b'^\\d{10}$', message=b'Tamanho maximo de 10 caracteres', code=b'numero invalido')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='Telefone',
            field=models.IntegerField(max_length=15, null=True, verbose_name=b'Telefone'),
        ),
    ]
