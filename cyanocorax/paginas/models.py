from django.db import models
from tinymce import models as tinymce_models

# Create your models here.
class Pagina(models.Model):
    opciones_estado = (('ed',  'En revisión'), ('pu',  'Publicado'))
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    texto = tinymce_models.HTMLField()
    estado = models.CharField(max_length=2,
                              choices=opciones_estado,
                              default='En revisión')
    ultima_revision = models.DateTimeField(auto_now=True)


class Noticia(Pagina):
    medio = models.CharField(max_length=255)
    url = models.URLField(blank=True, null=True)
    fecha_publicacion = models.DateTimeField()
