# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0018_auto_20141031_1537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atendimento',
            old_name='DataConsulta',
            new_name='ConsultaData',
        ),
    ]
