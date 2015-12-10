from django.core.context_processors import csrf
from menus.views import auth_menu
from paginas.models import Pagina
from django.shortcuts import render, render_to_response,  get_object_or_404
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponseRedirect


def one_of_this_perm(permisos: list,  request):
    '''
     Esta función es provisional, pero no se si sea útil  la idea es que
     ayude a controlar el acceso  a algunas operaciones pero en
     todo caso sería más  util en la aplicación de manejo de los corpus
     o las  colecciones directamente.
    '''

    gpermisos = request.user.get_all_permissions()
    if (not set(permisos) & set(gpermisos)):
        return (False)
    else:
        return (True)


def ingreso(request):
    state = "Por favor ingrese su usuario y contraseña..."
    username = password = ''
    context = {}
    context['NavBar'] = auth_menu(request, 'NavBar')
    context.update(csrf(request))

    next = "/"
    if request.GET:
        next = request.GET['next']

    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                state = "Su cuenta no está activa, por favor contactese\
                con el administrador."
        else:
            state = '<div style="color:red">\
            <span class="glyphicon glyphicon-warning-sign"></span> \
            Su usuario y/o su contraseña son incorrectos.</div>'

    context['state'] = state
    context['username'] = username
    context['next'] = next

    return render_to_response('ingreso.html', context)


def index(request):
    context = {}
    context['NavBar'] = auth_menu(request, 'NavBar')
    context['SideBar1'] = auth_menu(request, 'SideBar1')
    if request.user.is_authenticated():
        context['contenido'] = "<H1> Bienvenido </H1>"
        context['fullname'] = request.user.get_full_name()
    else:
        context['contenido'] = get_object_or_404(Pagina, titulo="Portada")
        if context['contenido'].texto:
            context['contenido'] = context['contenido'].texto
    return render(request, 'portada.html', context)
    # Con render_to_response no pasa los parámetros del request, y los
    # valores de los usuarios no son accesibles en el template.

# Create your views here.
