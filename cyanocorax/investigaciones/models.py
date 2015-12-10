from mongoengine import *
from datetime import *
from productos.models import Producto

class Investigacion(EmbeddedDocument):
    '''
    Documento de mongo que almacena las investigaciones relacionadas con los
    materiales de audio
    '''
    titulo = StringField(max_length=256)
    tituloCorto = StringField(max_length=256)
    descripcion = StringField(max_length=256)
    productos = ListField(EmbeddedDocumentField(Producto))
    fechaInicio = DateTimeField(default=now.date())
    fechaFin = DateTimeField(default=now.date())
