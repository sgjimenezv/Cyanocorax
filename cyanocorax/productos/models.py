from mongoengine import *

# Create your models here.

class Producto(Document):
    titulo = StringField(max_length=256)
    tipo = StringField(max_length=256)
    descripcion = StringField()
    referencia = StringField()
    enlace = URLField()

    def __unicode__(self):
        return self.titulo

    def __str__(self):
        return self.titulo
