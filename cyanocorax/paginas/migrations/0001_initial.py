# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('texto', tinymce.models.HTMLField()),
                ('estado', models.CharField(default='En revisión', max_length=2, choices=[('ed', 'En revisión'), ('pu', 'Publicado')])),
                ('ultima_revision', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('pagina_ptr', models.OneToOneField(serialize=False, to='paginas.Pagina', auto_created=True, parent_link=True, primary_key=True)),
                ('medio', models.CharField(max_length=255)),
                ('url', models.URLField(null=True, blank=True)),
                ('fecha_publicacion', models.DateTimeField()),
            ],
            bases=('paginas.pagina',),
        ),
    ]
