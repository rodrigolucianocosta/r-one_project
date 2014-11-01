# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimentofamiliar',
            name='AtendimentoF',
            field=models.ForeignKey(verbose_name=b'atendimento Familiar', to='atendimento.Atendimento'),
        ),
    ]
