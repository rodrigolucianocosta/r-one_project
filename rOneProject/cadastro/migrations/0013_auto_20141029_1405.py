# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0012_auto_20141029_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimentofamiliar',
            name='ComposicaoFamiliar1',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Composicao Familiar 1'),
        ),
        migrations.AlterField(
            model_name='atendimentofamiliar',
            name='ComposicaoFamiliar2',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Composicao Familiar 2'),
        ),
        migrations.AlterField(
            model_name='atendimentofamiliar',
            name='ComposicaoFamiliar3',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Composicao Familiar 3'),
        ),
        migrations.AlterField(
            model_name='atendimentofamiliar',
            name='ComposicaoFamiliar4',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Composicao Familiar 4'),
        ),
        migrations.AlterField(
            model_name='atendimentofamiliar',
            name='ComposicaoFamiliar5',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Composicao Familiar 5'),
        ),
    ]
