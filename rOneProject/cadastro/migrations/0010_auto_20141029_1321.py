# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0009_auto_20141029_1258'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cid',
            new_name='cidAdesao',
        ),
    ]
