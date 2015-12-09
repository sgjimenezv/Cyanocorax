from django.contrib import admin
from .models import Pagina, Noticia

# Register your models here.
@admin.register(Pagina)
class PaginaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'estado',  'ultima_revision')


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'estado',  'ultima_revision')
