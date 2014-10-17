# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0006_auto_20141016_0409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pessoa',
            name='NomeMae',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Nome da Mae'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='NomePai',
            field=models.CharField(max_length=50, null=True, verbose_name=b'Nome do Pai'),
            preserve_default=True,
        ),
    ]
