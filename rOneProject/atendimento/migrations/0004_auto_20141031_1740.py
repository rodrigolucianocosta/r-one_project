# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0003_auto_20141031_1739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atendimento',
            name='CartaoSus',
        ),
        migrations.AddField(
            model_name='atendimento',
            name='SalaAtendimento',
            field=models.IntegerField(max_length=10, null=True, verbose_name=b'Sala de Atendimento'),
            preserve_default=True,
        ),
    ]
