from mongoengine import *
from datetime import datetime
from django.db.models import Q
from django.contrib.auth.models import Group

# Create your models here.


class Producto(EmbeddedDocument):
    titulo = StringField(max_length=256)
    tipo = StringField(max_length=256)
    referencia = StringField()
    enlace = StringField(max_length=256)
