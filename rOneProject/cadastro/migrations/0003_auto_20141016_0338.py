# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_auto_20141015_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cid', models.IntegerField(null=True, verbose_name=b'Cid')),
                ('NomePessoa', models.CharField(max_length=100, null=True, verbose_name=b'Nome')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='subcadastro',
            name='Cadastro',
        ),
        migrations.DeleteModel(
            name='Cadastros',
        ),
        migrations.DeleteModel(
            name='SubCadastro',
        ),
    ]
