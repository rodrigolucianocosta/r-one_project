# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0006_auto_20141029_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=50, null=True, verbose_name=b'Tipo de Usuario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='TipoUsuario',
            field=models.ForeignKey(verbose_name=b'Tipo de Usuario', to='cadastro.TipoUsuario', null=True),
            preserve_default=True,
        ),
    ]
