from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Permisos(models.Model):
    '''
    Dado que las aplicaciones para manejo de aplicaciones utilizan mongo
    como base de datos y que la interfaz admnistrativa de Django no
    interractúa con los modelos que se guardan en mongo, se crea este
    modelo ficticcio para guardar todos los permisos realtivos a Corpus
    y Colecciones.
    En el futuro se agregarán funciones que mejoren esa interacción.
    '''

    opciones_permisos = (
        ('Explorar', 'Exp'),
        ('Administrar', 'Adm'),
        ('Crear', 'Cre'),
        ('Ver', 'Ver'),
        ('Descargar', 'Des'),
        ('Modificar', 'Mod'),
        ('Borrar', 'Bor'),
        )

    mongo_database = models.CharField(max_length=50)
    mongo_collection = models.CharField(max_length=50)
    mongo_element = models.CharField(max_length=50)
    permiso = models.CharField(max_length=2,
                               choices=opciones_permisos,
                               default='Exp')
    usuario = models.ManyToManyField(User)

    class Meta:
        permissions = (
            # Permisos del corpus
            ('creCorp_Permiso', 'Crear corpus'),
            ('addCorp_Permiso', 'Agreager elemento a corpus'),
            ('modCorp_Permiso', 'Modificar información de corpus'),
            ('verCorp_Permiso', 'Ver corpus'),
            ('veeCorp_Permiso', 'Ver elemento de corpus'),
            ('borCorp_Permiso', 'Borrar corpus'),
            ('susCorp_Permiso', 'Borrar elemento de corpus'),
            ('repCorp_Permiso', 'Reproducir corpus'),
            ('reeCorp_Permiso', 'Reproducir elemento de corpus'),
            ('desCorp_Permiso', 'Descargar corpus'),
            ('deeCorp_Permiso', 'Descargar elemento de corpus'),
            ('admCorp_Permiso', 'Administrar corpus'),
        )
