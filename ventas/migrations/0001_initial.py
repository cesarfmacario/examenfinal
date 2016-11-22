# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(max_length=7, primary_key=True, serialize=False)),
                ('nombre', models.TextField(default='')),
                ('foto', models.ImageField(upload_to='media/imagenes/')),
                ('marca', models.TextField(default='')),
                ('prunit', models.FloatField(default=0)),
                ('existencias', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('dpi', models.TextField()),
                ('nombre', models.TextField()),
            ],
        ),
    ]
