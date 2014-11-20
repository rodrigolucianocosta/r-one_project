# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0015_auto_20141029_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='atendimentofamiliar',
            name='NumeroMembrosFamiliares',
            field=models.IntegerField(max_length=10, null=True),
            preserve_default=True,
        ),
    ]
