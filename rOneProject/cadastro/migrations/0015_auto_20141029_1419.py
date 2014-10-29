# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0014_auto_20141029_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='Telefone',
            field=models.IntegerField(max_length=10, null=True, verbose_name=b'Telefone'),
        ),
    ]
