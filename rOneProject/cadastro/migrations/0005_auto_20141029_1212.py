# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_auto_20141029_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('pessoa_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cadastro.Pessoa')),
                ('Crm', models.CharField(max_length=10, null=True, verbose_name=b'Crm')),
            ],
            options={
            },
            bases=('cadastro.pessoa',),
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('pessoa_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cadastro.Pessoa')),
                ('CartaoSus', models.CharField(max_length=20, null=True, verbose_name=b'Cartao Sus')),
            ],
            options={
            },
            bases=('cadastro.pessoa',),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='Cor',
            field=models.CharField(max_length=10, null=True, verbose_name=b'Etinia'),
            preserve_default=True,
        ),
    ]
