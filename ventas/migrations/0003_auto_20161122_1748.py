# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_auto_20161122_1747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='prunit',
            new_name='precio_unitario',
        ),
    ]
