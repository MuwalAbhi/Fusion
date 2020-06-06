# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-06-05 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymkhana', '0003_auto_20200604_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration_form',
            name='branch',
            field=models.CharField(default='open', max_length=20),
        ),
        migrations.AlterField(
            model_name='registration_form',
            name='programme',
            field=models.CharField(default='open', max_length=20),
        ),
        migrations.AlterField(
            model_name='registration_form',
            name='roll',
            field=models.CharField(default='2016001', max_length=7, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='registration_form',
            name='user_name',
            field=models.CharField(default='Student', max_length=40),
        ),
    ]