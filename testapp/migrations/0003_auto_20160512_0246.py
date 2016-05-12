# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20160511_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calcu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('a', models.CharField(max_length=10)),
                ('b', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Doc',
        ),
    ]
