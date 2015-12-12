from mongoengine import *

# Create your models here.

class Producto(Document):
    titulo = StringField(max_length=256)
    tipo = StringField(max_length=256)
    descripcion = StringField()
    referencia = StringField()
    enlace = URLField()

    meta = {
        'indexes': [
            {'fields': ('titulo', 'tipo', 'referencia'), 'unique': True}
        ]
    }