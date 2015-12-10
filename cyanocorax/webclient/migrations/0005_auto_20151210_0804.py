# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webclient', '0004_auto_20151210_0744'),
    ]

    operations = [
        migrations.CreateModel(
            name='PermisosAudios',
            fields=[
                ('permisos_ptr', models.OneToOneField(serialize=False, to='webclient.Permisos', parent_link=True, primary_key=True, auto_created=True)),
            ],
            options={
                'permissions': (('addAudio_Permiso', 'Agregar audios al corpus'), ('delAudio_Permiso', 'Eliminar audios del corpus'), ('desAudio_Permiso', 'Descargar audio'), ('repAudio_Permiso', 'Reproducir audio'), ('marAudio_Permiso', 'Marcar')),
            },
            bases=('webclient.permisos',),
        ),
        migrations.CreateModel(
            name='PermisosCorpus',
            fields=[
                ('permisos_ptr', models.OneToOneField(serialize=False, to='webclient.Permisos', parent_link=True, primary_key=True, auto_created=True)),
            ],
            options={
                'permissions': (('creCorp_Permiso', 'Crear corpus'), ('addCorp_Permiso', 'Agregar elemento a corpus'), ('modCorp_Permiso', 'Modificar información de corpus'), ('verCorp_Permiso', 'Ver corpus'), ('veeCorp_Permiso', 'Ver elemento de corpus'), ('borCorp_Permiso', 'Borrar corpus'), ('susCorp_Permiso', 'Borrar elemento de corpus'), ('repCorp_Permiso', 'Reproducir corpus'), ('reeCorp_Permiso', 'Reproducir elemento de corpus'), ('desCorp_Permiso', 'Descargar corpus'), ('deeCorp_Permiso', 'Descargar elemento de corpus'), ('admCorp_Permiso', 'Administrar corpus')),
            },
            bases=('webclient.permisos',),
        ),
        migrations.CreateModel(
            name='PermisosInvestigaciones',
            fields=[
                ('permisos_ptr', models.OneToOneField(serialize=False, to='webclient.Permisos', parent_link=True, primary_key=True, auto_created=True)),
            ],
            options={
                'permissions': (('creInv_Permiso', 'Crear investigación'), ('delInv_Permiso', 'Borrar investigacion'), ('modInv_Permiso', 'Modificar investigacion'), ('verInv_permiso', 'Ver investigación'), ('addInv_permiso', 'Agregar Investigacion al corpus'), ('eliInv_permiso', 'Eliminar Investigacion del corpus')),
            },
            bases=('webclient.permisos',),
        ),
        migrations.CreateModel(
            name='PermisosProductos',
            fields=[
                ('permisos_ptr', models.OneToOneField(serialize=False, to='webclient.Permisos', parent_link=True, primary_key=True, auto_created=True)),
            ],
            options={
                'permissions': (('creProd_Permiso', 'Crear producto'), ('delProd_Permiso', 'Borrar producto'), ('modProd_Permiso', 'Modificar producto'), ('verProd_permiso', 'Ver producto'), ('addProd_Permiso', 'Agregar productos al corpus, las investigaciones o los audios'), ('eliProd_Permiso', 'Eliminar productos del corpus, las investigaciones o los audios')),
            },
            bases=('webclient.permisos',),
        ),
        migrations.AlterModelOptions(
            name='permisos',
            options={},
        ),
    ]
