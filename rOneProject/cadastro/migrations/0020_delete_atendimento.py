# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0019_auto_20141031_1550'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Atendimento',
        ),
    ]
