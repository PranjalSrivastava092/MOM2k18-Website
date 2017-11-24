# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 10:38
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('address', models.TextField(max_length=2000)),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex=b'^\\+?1?\\d{9,15}$')])),
                ('institute', models.CharField(max_length=1000)),
                ('event', multiselectfield.db.fields.MultiSelectField(choices=[(b'TME', b'MODELEXPO'), (b'IIP', b'Brainwave'), (b'QUIZ', b'Quiz'), (b'APP', b'Apps Corner'), (b'Flash', b'Rangmanch'), (b'OSD', b'Creations')], max_length=100)),
                ('message', models.TextField(blank=True, max_length=2000)),
            ],
        ),
    ]
