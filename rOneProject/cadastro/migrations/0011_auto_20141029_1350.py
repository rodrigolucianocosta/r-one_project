# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0010_auto_20141029_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='AtendimentoFamiliar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('PlanoIntervencao', models.CharField(max_length=50, null=True, verbose_name=b'Plano de Intervencao')),
                ('Paciente', models.ForeignKey(to='cadastro.Paciente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='atendimento',
            name='Paciente',
        ),
    ]
