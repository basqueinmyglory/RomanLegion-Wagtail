# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 17:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorsIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('name', models.CharField(max_length=250)),
                ('height', models.CharField(max_length=25)),
                ('age', models.CharField(max_length=2)),
                ('location', models.CharField(max_length=250)),
                ('routine', models.CharField(max_length=50)),
                ('diet', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
