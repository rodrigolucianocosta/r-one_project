# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0010_auto_20141024_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='atendimento',
            name='Consulta',
            field=models.OneToOneField(null=True, to_field=b'Marcacao da Consulta', to='cadastro.Pessoa'),
            preserve_default=True,
        ),
    ]
