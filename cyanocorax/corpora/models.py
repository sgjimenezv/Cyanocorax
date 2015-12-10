from mongoengine import *
from datetime import datetime
from django.db.models import Q
from menus.models import MenuItem, Menu
from django.contrib.auth.models import Group

# Create your models here.

class Tag(EmbeddedDocument):
     nombre = StringField(max_length=60,  required=True,  unique=True)
     nombreCSV = StringField(max_length=60,  required=True,  unique=True)
     equivalenteTEI = StringField(max_length=60)
     equivalenteIMDI = StringField(max_length=60)
     equivalenteOLAC = StringField(max_length=60)
     obligatorio = BooleanField(required=True)
     indexar = BooleanField(required=True)
     valor = DynamicField(required=True)

class CategoriaDeMetadatos(Document):
     nombre = StringField(max_length=60,  required=True,  unique=True)
     nombreCSV = StringField(max_length=60,  required=True,  unique=True)
     equivalenteTEI = StringField(max_length=60)
     equivalenteIMDI =StringField(max_length=60)
     equivalenteOLAC =StringField(max_length=60)
     tags = ListField(EmbeddedDocumentField(Tag))

class Corpus(DynamicDocument):
    def create_menu_item(self):
        '''
        Crea la entrada de menu para el corpus.
        '''
        entrada_menu = MenuItem()
        entrada_menu.texto = self.tituloCorto
        entrada_menu.clase = 'it'
        entrada_menu.aprobacion = 'au'
        entrada_menu.destino = '/corpus/explorar/'+self.tituloCorto
        entrada_menu.padre = MenuItem.objects.get(texto='Explorar corpus')
        entrada_menu.peso = 0
        entrada_menu.save()
        entrada_menu.rol = Group.objects.exclude(
            Q(name='Invitado') | Q(name='Usuario')
        )
        entrada_menu.save()

        Menu.objects.get(texto='NavBar').items.add(entrada_menu)
        Menu.objects.get(texto='SideBar1').items.add(entrada_menu)

    def delete_menu_item(self):
        '''
        Borra del corpus del menu.
        '''
        MenuItem.objects.filter(texto=self.tituloCorto).delete()
        "Borrar la entriada del menu cuando se borre la colección"

    def guardar(self):
        '''
        Guarda el corpus en la base de datos y crea la entrada de menu
        correspondiente
        '''
        self.save()
        self.create_menu_item()

    def eliminar(self):
        '''
        Elimina el corpus y de la base de datos y elimina la entrada de menu
        correspondiente
        '''
        self.delete_menu_item()
        self.delete()

    titulo = StringField(max_length=60,  required=True,  unique=True)
    tituloCorto = StringField(max_length=30,  required=True)
    creador = StringField(max_length=30,  required=True)
    fechaCreacion = DateTimeField(default=datetime.now())
    descripcionCorta = StringField(max_length=256)
    descripcion = StringField()

    # Definicipon de la estructura de metadatos
    #categoriasDeMetadatos = ListField(EmbeddedDocumentField(Tag))

    # Ruta a los archivos de audio
    #rutaArchivos = StringField()

    # Archivos de audio
    #audios = ListField()
