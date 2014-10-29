# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_auto_20141025_1926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='DataNascimento',
            new_name='NascimentoData',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='cid',
        ),
    ]
