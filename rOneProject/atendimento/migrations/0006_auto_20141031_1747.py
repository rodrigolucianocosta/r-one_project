# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atendimento', '0005_auto_20141031_1746'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='atendimentofamiliar',
            options={'verbose_name': 'Atendimento Familiar', 'verbose_name_plural': 'Atendimento Familiar'},
        ),
    ]
