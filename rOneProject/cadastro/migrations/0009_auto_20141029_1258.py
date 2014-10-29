# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0008_cid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cid',
            name='doenca',
        ),
        migrations.AddField(
            model_name='cid',
            name='descricao',
            field=models.CharField(max_length=100, null=True, verbose_name=b'descriacao do cid'),
            preserve_default=True,
        ),
    ]
