# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0007_auto_20141209_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimentofamiliar',
            name='TipoAtendimento',
            field=models.CharField(max_length=1, null=True, verbose_name=b'Tipo Atendimento', choices=[(b'A', b'RETORNO'), (b'B', b'CONSULTA'), (b'C', b'AGENDAMENTO')]),
        ),
    ]
