from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Permisos(models.Model):
    '''
    Dado que las aplicaciones para manejo de corpus utilizan mongo
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


class PermisosCorpus(Permisos):
    class Meta:
        '''
        Permisos explicitos provicionales para corpus, la idea es que en el futuro estos
        permisos se manejen con la clase principal y funciones especializadas.
        '''
        permissions = (
            ('creCorp_Permiso', 'Crear corpus'),
            ('addCorp_Permiso', 'Agregar elemento a corpus'),
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

class PermisosInvestigaciones(Permisos):
    class Meta:
        '''
        Permisos explicitos provicionales para corpus, la idea es que en el futuro estos
        permisos se manejen con la clase principal y funciones especializadas.
        '''
        permissions = (
            ('creInv_Permiso', 'Crear investigación'),
            ('delInv_Permiso', 'Borrar investigacion'),
            ('modInv_Permiso', 'Modificar investigacion'),
            ('verInv_permiso', 'Ver investigación'),
            ('addInv_permiso', 'Agregar Investigacion al corpus'),
            ('eliInv_permiso', 'Eliminar Investigacion del corpus'),
        )

class PermisosProductos(Permisos):
    class Meta:
        '''
        Permisos explicitos provicionales para corpus, la idea es que en el futuro estos
        permisos se manejen con la clase principal y funciones especializadas.
        '''
        permissions = (
            ('creProd_Permiso', 'Crear producto'),
            ('delProd_Permiso', 'Borrar producto'),
            ('modProd_Permiso', 'Modificar producto'),
            ('verProd_permiso', 'Ver producto'),
            ('addProd_Permiso', 'Agregar productos al corpus, las investigaciones o los audios'),
            ('eliProd_Permiso', 'Eliminar productos del corpus, las investigaciones o los audios'),
        )

class PermisosAudios(Permisos):
    class Meta:
        '''
        Permisos explicitos provicionales para corpus, la idea es que en el futuro estos
        permisos se manejen con la clase principal y funciones especializadas.
        '''
        permissions = (
            ('addAudio_Permiso', 'Agregar audios al corpus'),
            ('delAudio_Permiso', 'Eliminar audios del corpus'),
            ('desAudio_Permiso', 'Descargar audio'),
            ('repAudio_Permiso', 'Reproducir audio'),
            ('marAudio_Permiso', 'Marcar'),

        )
