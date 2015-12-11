from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Producto
from menus.views import auth_menu
from django.core import serializers
from django.http import HttpResponse
import json 

# Create your views here.

@login_required(login_url='/login')
def explorar_productos(request):
    context={}
    context['objetivo'] = 'Detalles'
    context['productos'] = Producto.objects.all()
    context['NavBar'] = auth_menu(request, 'NavBar')
    context['SideBar1'] = auth_menu(request, 'SideBar1')
    return render(request, 'explorar_productos.html', context)

@login_required(login_url='/login')
def explorar_productos_json(request):
    #productos = Producto.objects.all().to_json()
    #productos2 = Producto.to_json()#.all()
    #print(dir(Producto))
    #for(x in productos):
    #print(productos2)
    #data = {}
    #data=json.dumps(list(Producto.objects.all().values()))
    data = Producto.objects.to_json() 

    #data = serializers.serialize("json",productos)
    return HttpResponse(data, content_type='application/json')

@login_required(login_url='/login')
def modificar_productos(request):
    context={}
    context['objetivo'] = 'Modificar'
    context['productos'] = Producto.objects.all()
    context['NavBar'] = auth_menu(request, 'NavBar')
    context['SideBar1'] = auth_menu(request, 'SideBar1')
    return render(request, 'explorar_productos.html', context)
