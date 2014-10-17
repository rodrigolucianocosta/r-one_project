# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_auto_20141016_0338'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='Cpf',
            field=models.CharField(max_length=14, null=True, verbose_name=b'Cpf'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='Rg',
            field=models.CharField(max_length=20, null=True, verbose_name=b'Rg', blank=True),
            preserve_default=True,
        ),
    ]
