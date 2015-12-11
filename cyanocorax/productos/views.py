from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Producto
from menus.views import auth_menu
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
def modificar_productos(request):
    context={}
    context['objetivo'] = 'Modificar'
    context['productos'] = Producto.objects.all()
    context['NavBar'] = auth_menu(request, 'NavBar')
    context['SideBar1'] = auth_menu(request, 'SideBar1')
    return render(request, 'explorar_productos.html', context)

@login_required(login_url='/login')
def producto_detalles(request, producto_id):
    context={}
    print(">>>>>>>>>>>>>>>>>>producto_id")
    print(producto_id)
    context['producto'] = Producto.objects.get(id=producto_id)
    context['NavBar'] = auth_menu(request, 'NavBar')
    context['SideBar1'] = auth_menu(request, 'SideBar1')
    return render(request, 'explorar_productos.html', context)
