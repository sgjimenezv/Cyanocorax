#from django.test import TestCase
from corpora.models import Corpus

# Create your tests here.
Corpus.objects.create(
    titulo="lion",
    tituloCorto="l",
    creador="me",
    name="lion",
    sound="roar",
    participante={
        'nombre_completo':{
            'nombre':'Juan Carlos',
            'apellido':'López Rodríguez',
            }
        }
    )

Corpus.objects.create(
    titulo="cat",
    tituloCorto="c",
    name="cat",
    creador="me",
    sound="meow")
