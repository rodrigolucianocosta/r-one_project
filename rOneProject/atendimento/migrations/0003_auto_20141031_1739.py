# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0002_auto_20141031_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atendimento',
            name='NomeAtendimento',
        ),
        migrations.AddField(
            model_name='atendimento',
            name='CartaoSus',
            field=models.IntegerField(max_length=10, null=True, verbose_name=b'Numero do CartaoSus'),
            preserve_default=True,
        ),
    ]
