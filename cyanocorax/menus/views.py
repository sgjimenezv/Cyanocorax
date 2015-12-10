from django.shortcuts import render
from .models import Menu

# Create your views here.
def auth_menu(request, menu):
    auth_menu = []
    secciones = Menu.objects.get(texto=menu).items.all()
    secciones = secciones.filter(clase='se').order_by('peso')
    for seccion in secciones:
        seccion.inject_request(request)
        if (seccion.is_in_menu(menu) and seccion.element_group_auth()):
            auth_menu.append(seccion.get_descendencia(menu))
    return auth_menu
