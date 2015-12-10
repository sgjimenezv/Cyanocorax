from django.db import models
from django.contrib.auth.models import Group
# Create your models here.

class MenuItem(models.Model):
    '''
    Este modelo almacenera cualquier entrada de menú, por ahora estas
    entradas deben ser asignadas a un menu particular en el modelo Menu
    '''

    def __str__(self):
        '''
        Este metodo devuelve un string para los objetos  MenuItem,
        facilitando su impresión y por tanto su uso en plantillas
        '''
        return self.texto

    def __lt__(self, other):
        '''
        Es método implementa una regla de ordenamiento para los objetos
        MenuItem, facilitando la operación con ellos una vez estan fuera
        de la base de datos (si por ejemplo son convertidos en listas,
        tuplas, diccionarios, etc)
        '''
        return self.peso < self.peso

    def inject_request(self, request):
        '''
        Esta función inyecta el REQUEST de las vistas en el modelo
        '''
        self.request = request

    def is_in_menu(self,  menu):
        '''
        Esta función comprueba si el elemento pertenece a un menu
        determinado.
        '''
        if Menu.objects.filter(items=self.id):
            return True
        return False

    def element_group_auth(self):
        '''
        Esta función comprueba si el usuario esta autorizado para ver este
        elemento
        '''

        if (self.request.user.is_anonymous() and
                self.aprobacion == 'an'or self.aprobacion == 'am'):
            return True
        if (self.request.user.is_authenticated()):
            if (self.request.user.is_superuser):
                if (self.aprobacion == 'au' or self.aprobacion == 'am'):
                    return True
                if (self.aprobacion == 'an'):
                    return False
            if ((set(self.rol.all()) &
                    set(self.request.user.groups.all())) or not self.rol):

                return True
        return False

    def get_descendencia(self,  menu):
        '''
        Esta función devuelve un diccionario con  hijos y nietos del
        objeto MenuItem, facilitando la creación de arreglos para
        pasarselos a las funciones que crean los menus.
        También comprueba que el elemeto este autorizado para ese menu y
        para el grupo al que pertenece el usuario.
        '''
        if (self.is_in_menu(menu) and self.element_group_auth()):
            descendencia = dict()
            descendencia['elemento'] = self
            descendencia['hijos'] = []
            for hijo in MenuItem.objects.filter(padre=self).order_by('peso'):
                hijo.inject_request(self.request)
                descendencia['hijos'].append(hijo.get_descendencia(menu))
            if not descendencia['hijos']:
                descendencia['hijos'] = False
            return descendencia

    opciones_menu = (('it', 'Entrada'),
                     ('se', 'Sección'),
                     ('en',  'encabezado'))
    opciones_aprobacion = (('au', 'Autenticado'),
                           ('an', 'Anonimo'),
                           ('am', 'ambos'))
    texto = models.CharField(max_length=50)
    clase = models.CharField(max_length=2,
                             choices=opciones_menu,
                             default='Entrada')
    rol = models.ManyToManyField(Group,  blank=True)
    aprobacion = models.CharField(max_length=2,
                                  choices=(('au', 'Autenticado'),
                                           ('an', 'Anonimo'),
                                           ('', '')),
                                  default='Autenticado')
    destino = models.CharField(max_length=256, default="/")
    padre = models.ForeignKey('self',
                              blank=True,
                              null=True,
                              on_delete=models.SET_NULL,)
    peso = models.SmallIntegerField()

    class Meta:
        get_latest_by = '-peso'
        order_with_respect_to = 'padre'
        ordering = ['padre', 'clase', 'peso']


class Menu(models.Model):
    def __str__(self):
        return self.texto
    texto = models.CharField(max_length=50)
    rol = models.ManyToManyField(Group,  blank=True)
    items = models.ManyToManyField(MenuItem, blank=True,  related_name='menus')
