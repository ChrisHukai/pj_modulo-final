# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-28 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exemplo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64, verbose_name='Nome')),
                ('atributo2', models.IntegerField(verbose_name='Atributo2')),
                ('atributo3', models.BooleanField(verbose_name='Atributo3')),
            ],
        ),
    ]
