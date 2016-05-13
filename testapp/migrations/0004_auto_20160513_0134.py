# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20160512_0246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calcu',
            old_name='a',
            new_name='n',
        ),
        migrations.RemoveField(
            model_name='calcu',
            name='b',
        ),
    ]
