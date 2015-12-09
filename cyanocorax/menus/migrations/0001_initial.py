# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('texto', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('texto', models.CharField(max_length=50)),
                ('clase', models.CharField(default='Entrada', max_length=2, choices=[('it', 'Entrada'), ('se', 'Sección'), ('en', 'encabezado')])),
                ('aprobacion', models.CharField(default='Autenticado', max_length=2, choices=[('au', 'Autenticado'), ('an', 'Anonimo'), ('', '')])),
                ('destino', models.CharField(default='/', max_length=256)),
                ('peso', models.SmallIntegerField()),
                ('padre', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='menus.MenuItem', null=True, blank=True)),
                ('rol', models.ManyToManyField(blank=True, to='auth.Group')),
            ],
            options={
                'ordering': ['padre', 'clase', 'peso'],
                'get_latest_by': '-peso',
            },
        ),
        migrations.AddField(
            model_name='menu',
            name='items',
            field=models.ManyToManyField(blank=True, related_name='menus', to='menus.MenuItem'),
        ),
        migrations.AddField(
            model_name='menu',
            name='rol',
            field=models.ManyToManyField(blank=True, to='auth.Group'),
        ),
        migrations.AlterOrderWithRespectTo(
            name='menuitem',
            order_with_respect_to='padre',
        ),
    ]
