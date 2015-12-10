# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webclient', '0002_auto_20151210_0650'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='permisos',
            options={'permissions': (('creCorp_Permiso', 'Crear corpus'), ('addCorp_Permiso', 'Agreager elemento a corpus'), ('modCorp_Permiso', 'Modificar información de corpus'), ('verCorp_Permiso', 'Ver corpus'), ('veeCorp_Permiso', 'Ver elemento de corpus'), ('borCorp_Permiso', 'Borrar corpus'), ('susCorp_Permiso', 'Borrar elemento de corpus'), ('repCorp_Permiso', 'Reproducir corpus'), ('reeCorp_Permiso', 'Reproducir elemento de corpus'), ('desCorp_Permiso', 'Descargar corpus'), ('deeCorp_Permiso', 'Descargar elemento de corpus'), ('admCorp_Permiso', 'Administrar corpus'), ('creInv_Permiso', 'Crear investigación'), ('delInv_Permiso', 'Borrar investigacion'), ('modInv_Permiso', 'Modificar investigacion'), ('verInv_permiso', 'Ver investigación'), ('addInv_permiso', 'Agregar Investigacion al corpus'), ('eliInv_permiso', 'Eliminar Investigacion del corpus'), ('creProd_Permiso', 'Crear investigación'), ('delProd_Permiso', 'Borrar investigacion'), ('modProd_Permiso', 'Modificar investigacion'), ('verProd_permiso', 'Ver investigación'), ('addProd_Permiso', 'Agregar productos al corpus, las investigaciones o los audios'), ('eliProd_Permiso', 'Eliminar productos del corpus, las investigaciones o los audios'), ('addAudio_Permiso', 'Agregar audios al corpus'), ('delAudio_Permiso', 'Eliminar audios del corpus'), ('marAudio_Permiso', 'Marcar'))},
        ),
    ]
