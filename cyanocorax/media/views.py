from datetime import datetime
from django.contrib.auth.decorators import login_required,  permission_required
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest, StreamingHttpResponse
from django.core.context_processors import csrf
from .models import MediaCollection, MediaCollectionRoot
from .forms import CrearColeccion
#from cyanocoraxwebgui.views import auth_menu
#from cyanocoraxapi.views import json_process_request



#@login_required(login_url='/login')
#@permission_required('cyanocoraxauth.verColl_Permiso', login_url='/login')
def titulos(request):
    titulos = []
    for coleccion in MediaCollection.objects.only('titulo'):
        if coleccion.titulo:
            titulos.append(coleccion.titulo)
    return JsonResponse(titulos,  safe=False)


#@login_required(login_url='/login')
#@permission_required('cyanocoraxauth.verColl_Permiso', login_url='/login')
def ubicaciones(request):
    ubicaciones = []
    for coleccion in MediaCollection.objects.only('ubicacionColeccion'):
        if coleccion.ubicacionColeccion:
            ubicaciones.append(coleccion.ubicacionColeccion.ruta)
    return JsonResponse(ubicaciones,  safe=False)

#@login_required(login_url='/login')
#@permission_required('cyanocoraxauth.verColl_Permiso', login_url='/login')
def titulosCortos(request):
    titulosCortos = []
    for coleccion in MediaCollection.objects.only('tituloCorto'):
        if coleccion.tituloCorto:
            titulosCortos.append(coleccion.tituloCorto)
    return JsonResponse(tituloCorto,  safe=False)

#@login_required(login_url='/login')
#@permission_required('cyanocoraxauth.creColl_Permiso',   login_url='/login')
def crear_coleccion(request):
    context = {}
    #context['NavBar'] = auth_menu(request, 'NavBar')
    #context['SideBar1'] = auth_menu(request, 'SideBar1')
    context['form'] = CrearColeccion()
    context['titulos'] = titulos(request).content
    context['ubicaciones'] = ubicaciones(request).content
    context.update(csrf(request))
    errores = ""
    if request.method == 'POST':
        #json_process_request(request)
        context['form'] = CrearColeccion(request.POST)
        if context['form'].is_valid():
            coleccion = MediaCollection()
            ruta = MediaCollectionRoot()
            ruta.ruta = context['form'].cleaned_data.get('collection_location')
            coleccion.titulo =  context['form'].cleaned_data.get('collection_name')
            coleccion.tituloCorto =  context['form'].data.get('collection_short_name')
            coleccion.creador =  "%s" %request.user
            coleccion.ubicacionColeccion =  ruta
            coleccion.descripcionCorta =  context['form'].cleaned_data.get('collection_short_description')
            coleccion.descripcion =  context['form'].cleaned_data.get('collection_description')

            print("mirar el audio ")
            print(coleccion.audio)
            print("mirar el audio ")
            actualizar_audios(request, coleccion)

            print('bien antes de guardar')
            print(coleccion.audio)
            coleccion.guardar()
            print("disque guardo la informacion")
            print("...........")
        else:
            return HttpResponseBadRequest(context['form'].errors.as_json())
    return render(request, 'crear_coleccion.html', context)


#@login_required(login_url='/login')
def actualizar_audios(request, coleccion):
    print ("Yuhuuuuuuuuuuuuuuuuuuu")
    #dato quemado .mp3
    response=coleccion.update_audios(["mp3"])
    return response

#@login_required(login_url='/login')
def explorar_coleccion(request, coleccion):
    context={}
    collection = MediaCollection.objects.get(tituloCorto=coleccion)
    context['titulo']=collection.titulo
    context['tituloCorto']=coleccion
    context['descripcionCorta']= collection.descripcionCorta
    context['descripcion']= collection.descripcion
    context['audios'] = collection.audio
    #context['NavBar'] = auth_menu(request, 'NavBar')
    #context['SideBar1'] = auth_menu(request, 'SideBar1')
    return render(request, 'explorar_coleccion.html', context)








########
########
########
########
########
########
########
########

from django.shortcuts import render
from media.tasks import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
import json
from media.forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt
from media.models import Audio_mdl
from celery.result import AsyncResult

# Create your views here.


@csrf_exempt
def pruebaSuma(reques):

   
    #resultado = mul.delay(1,3).get()
    #print(mul.delay(1,3))
    result = add.apply_async((2, 2), countdown=3)
    resultado = result.get()

    json_data = json.dumps(resultado)

    return HttpResponse(json_data,content_type='application/json')



@csrf_exempt
def convertirAudio(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            #handle_uploaded_file(request.FILES['audioFile'])
            form.save()
            return HttpResponseRedirect('/success/url/')

    else:
        form = UploadFileForm()
    #return render_to_response('upload.html', {'form': form})
   
    #resultado = mul.delay(1,3).get()
    #print(mul.delay(1,3))
    #result = add.apply_async((2, 2), countdown=3)
    #resultado = result.get()

    #json_data = json.dumps(resultado)

    return render_to_response('formulario-audio.html', {'form': form})



def formularioRegistroColeccion(request):
    form = CrearColeccion()
    return render(request,'formulario-collection.html',{'form':form})



def detalleAudio(request,id_audio):
    print('hola ? ')
    audio=Audio_mdl.objects.filter(id=id_audio)
    print(audio)
    context = {'audio':audio}
    return render(request,'detalle-audio.html',context)

def stremerAudio(request,id_audio):
    audio=Audio_mdl.objects.get(id=id_audio)
    ruta = audio.audioFile
    return ogg_stream_response(request,ruta)
    #conversion = ogg_stream_response.apply_async((request,ruta))
    #return conversion.get()
    

def generarAudio(request,id_audio,formato):
    audio=Audio_mdl.objects.get(id=id_audio)
    ruta = audio.audioFile

    pass


def handle_uploaded_file(f):
    print(f)
    pass
    #with open('some/file/name.txt', 'wb+') as destination:
    #    for chunk in f.chunks():
    #        destination.write(chunk)

