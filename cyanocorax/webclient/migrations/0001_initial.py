# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Permisos',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('mongo_database', models.CharField(max_length=50)),
                ('mongo_collection', models.CharField(max_length=50)),
                ('mongo_element', models.CharField(max_length=50)),
                ('permiso', models.CharField(choices=[('Explorar', 'Exp'), ('Administrar', 'Adm'), ('Crear', 'Cre'), ('Ver', 'Ver'), ('Descargar', 'Des'), ('Modificar', 'Mod'), ('Borrar', 'Bor')], max_length=2, default='Exp')),
                ('usuario', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('creCorp_Permiso', 'Crear corpus'), ('addCorp_Permiso', 'Agreager elemento a corpus'), ('modCorp_Permiso', 'Modificar información de corpus'), ('verCorp_Permiso', 'Ver corpus'), ('veeCorp_Permiso', 'Ver elemento de corpus'), ('borCorp_Permiso', 'Borrar corpus'), ('susCorp_Permiso', 'Borrar elemento de corpus'), ('repCorp_Permiso', 'Reproducir corpus'), ('reeCorp_Permiso', 'Reproducir elemento de corpus'), ('desCorp_Permiso', 'Descargar corpus'), ('deeCorp_Permiso', 'Descargar elemento de corpus'), ('admCorp_Permiso', 'Administrar corpus')),
            },
        ),
    ]
