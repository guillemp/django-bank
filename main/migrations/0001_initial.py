# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('number', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=240)),
                ('date', models.DateField(null=True, blank=True)),
                ('more', models.CharField(max_length=240)),
                ('amount', models.DecimalField(default=Decimal('0.00'), max_digits=8, decimal_places=2)),
                ('balance', models.DecimalField(default=Decimal('0.00'), max_digits=8, decimal_places=2)),
                ('hash_code', models.CharField(max_length=128)),
                ('account', models.ForeignKey(to='main.Account')),
                ('category', models.ForeignKey(blank=True, to='main.Category', null=True)),
            ],
        ),
    ]
