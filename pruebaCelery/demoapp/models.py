from mongoengine import *
from datetime import datetime
from Crypto.Cipher import ARC4
from os import urandom
from base64 import b64encode, b64decode
from django.db.models import Q
from demoapp.media import metadata, buscar_audios_local
#from cyanocoraxwebgui.models import MenuItem, Menu
from django.contrib.auth.models import Group
# from CyanocoraxAuth.models import Permisos

'''
Esta aplicación y por tanto estos modelos, tendrán por objetivo
manipilar facilmente los audios no catalogados o marcados
que haran parte de un corpus en el futuro.

A medida que los audios se seleccionen y modifiquen, irán haciendo
parte de un corpus
'''


def get_value(name):
    def f(self):
        return MediaCollectionRoot.decrypt(getattr(self, 'e_ %s' %name))
    return f


def set_value(name):
    def f(self, value):
        setattr(self, 'e_%s' %name, MediaCollectionRoot.encrypt(value))
    return f


class Producto(EmbeddedDocument):
    titulo = StringField(max_length=256)
    tipo = StringField(max_length=256)
    referencia = StringField(max_length=256)
    enlace = StringField(max_length=256)


class Proyecto(EmbeddedDocument):
    titulo = StringField(max_length=256)
    tituloCorto = StringField(max_length=256)
    descripcion = StringField(max_length=256)
    productos = ListField(EmbeddedDocumentField(Producto))
    fechaInicio = DateTimeField()
    fechaFin = DateTimeField()


class Media(DynamicEmbeddedDocument):
    nombreArchivo = StringField(max_length=256)
    ubicacionArchivo = StringField(max_length=256)
    md5 = StringField(max_length=32)
    tamanoArchivo = IntField()
    productos = ListField(EmbeddedDocumentField(Producto))
    meta = {'allow_inheritance': True}


class MediaAudio(Media):
    nombre_del_codec = StringField(max_length=15)
    nombre_largo_del_codec = StringField(max_length=150)
    base_temporal_del_codec = StringField(max_length=15)
    formato_de_muestreo = StringField(max_length=5)
    frecuencia_de_muestreo = IntField(max_value=96000)
    canales = IntField(max_value=16,  min_value=1)
    bits_por_muestra = IntField(max_value=64,  min_value=2)
    tasa_de_bits = IntField()
    bits_por_muestra_en_bruto = IntField(max_value=64,  min_value=2)
    muestras = IntField()
    duracion = DecimalField(precision=6)
    ieng = StringField(max_length=32)
    encoder_software = StringField(max_length=50)
    fecha_digitalizacion = DateTimeField()


class AdicionalFormat(EmbeddedDocument):
    format = StringField(max_length=5)
    item = EmbeddedDocumentField(MediaAudio)


class MediaCollectionRoot(EmbeddedDocument):
    SALT_SIZE = 8

    LocalRemote = BinaryField()
    ruta = StringField(max_length=128, unique=True)
    e_username = StringField()
    e_password = StringField()
    e_host = StringField()

    @staticmethod
    def encrypt(plaintext):
        salt = urandom(Password.SALT_SIZE)
        arc4 = ARC4.new(salt + settings.SECRET_KEY)
        plaintext = "%3d%s%s" % (len(plaintext),
                                 plaintext,
                                 urandom(256-len(plaintext))
                                 )
        return "%s$%s" % (b64encode(salt), b64encode(arc4.encrypt(plaintext)))

    @staticmethod
    def decrypt(ciphertext):
        salt, ciphertext = map(b64decode, ciphertext.split('$'))
        arc4 = ARC4.new(salt + settings.SECRET_KEY)
        plaintext = arc4.decrypt(ciphertext)
        return plaintext[3:3+int(plaintext[:3].strip())]

    def encrypted_property(name):
        return property(get_value(name), set_value(name))

    username = encrypted_property('username')
    password = encrypted_property('password')
    host = encrypted_property('host')


class MediaCollection(Document):

    def create_menu_item(self):
        "Crear la entrada de menu cuando se cree la colección"
        #entrada_menu = MenuItem()
        entrada_menu.texto = self.tituloCorto
        entrada_menu.clase = 'it'
        entrada_menu.aprobacion = 'au'
        entrada_menu.destino = '/colecciones/explorar/'+self.tituloCorto
        #entrada_menu.padre = MenuItem.objects.get(texto='Explorar colecciones')
        entrada_menu.peso = 0
        entrada_menu.save()
        entrada_menu.rol = Group.objects.exclude(
            Q(name='Invitado') | Q(name='Usuario')
        )
        entrada_menu.save()

        #Menu.objects.get(texto='NavBar').items.add(entrada_menu)
        #Menu.objects.get(texto='SideBar1').items.add(entrada_menu)

    def delete_menu_item(self):
        pass
       # MenuItem.objects.filter(texto=self.tituloCorto).delete()
        "Borrar la entriada del menu cuando se borre la colección"

    def guardar(self):
        self.save()
        #self.create_menu_item()

    def eliminar(self):
        self.delete_menu_item()
        self.delete()

    def agregar_audios(self, file):
        self.audio.append(metadata(file))
        return ("archivo agregado: {0}".format(file))

    def update_audios(self, formatos):
        contador_de_archivos = 0
        total_audios = 0
        for formato in formatos:
            allfilesTemp = buscar_audios_local.apply_async((self.ubicacionColeccion.ruta, formato))
            allfiles = allfilesTemp.get()
            total_audios += allfiles[1]
            for file in allfiles[0]:
                contador_de_archivos = contador_de_archivos + 1
                porcentaje = contador_de_archivos*100/total_audios
                self.agregar_audios(file)


    titulo = StringField(max_length=60,  required=True,  unique=True)
    tituloCorto = StringField(max_length=30,  required=True, unique=True)
    creador = StringField(max_length=30,  required=True)
    fecha_creacion = DateTimeField(default=datetime.now())
    ubicacionColeccion = EmbeddedDocumentField(MediaCollectionRoot, unique=True)
    descripcionCorta = StringField(max_length=256)
    descripcion = StringField()
    proyecto = ListField(EmbeddedDocumentField(Proyecto))
    audio = ListField(EmbeddedDocumentField(MediaAudio))
    formatos = ListField(EmbeddedDocumentField(AdicionalFormat))
    pub_date = DateTimeField(help_text='date published')
    numero_archivos = IntField()
    log_de_creacion = StringField()
    log_de_modificacion = StringField()




from django.db import  models 

### borrar pruebas !!!!
class Audio_mdl(models.Model):
    nombre = models.CharField(max_length=200)
    audioFile = models.FileField(upload_to='audios/')