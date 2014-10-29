# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0011_auto_20141029_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='atendimentofamiliar',
            name='ComposicaoFamiliar1',
            field=models.CharField(max_length=50, null=True, verbose_name=b'ComposicaoFamiliar 1'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='atendimentofamiliar',
            name='ComposicaoFamiliar2',
            field=models.CharField(max_length=50, null=True, verbose_name=b'ComposicaoFamiliar 2'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='atendimentofamiliar',
            name='ComposicaoFamiliar3',
            field=models.CharField(max_length=50, null=True, verbose_name=b'ComposicaoFamiliar 3'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='atendimentofamiliar',
            name='ComposicaoFamiliar4',
            field=models.CharField(max_length=50, null=True, verbose_name=b'ComposicaoFamiliar 4'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='atendimentofamiliar',
            name='ComposicaoFamiliar5',
            field=models.CharField(max_length=50, null=True, verbose_name=b'ComposicaoFamiliar 5'),
            preserve_default=True,
        ),
    ]
