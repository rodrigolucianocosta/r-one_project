# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0007_auto_20141029_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cidPessoa', models.CharField(max_length=50, null=True, verbose_name=b'numero do cid')),
                ('doenca', models.ForeignKey(to='cadastro.Paciente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
