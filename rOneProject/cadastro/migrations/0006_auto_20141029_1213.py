# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0005_auto_20141029_1212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='Cor',
            new_name='Etinia',
        ),
    ]
