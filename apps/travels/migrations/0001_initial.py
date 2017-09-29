# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 18:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('logreg', '0002_remove_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dest', models.CharField(max_length=255)),
                ('descr', models.CharField(max_length=255)),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('joined_by', models.ManyToManyField(related_name='joined_trips', to='logreg.User')),
                ('planned_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planned_trips', to='logreg.User')),
            ],
        ),
    ]
