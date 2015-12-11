import fnmatch
import os
from celery import shared_task
from celery.decorators import task 
from celery.utils.log import get_task_logger

from subprocess import Popen, PIPE # Esta librería es para interactuar con el shell de linux
from shlex import split # Esta librería permite dividir los parametros de un comando de shell en una lista
from ast import literal_eval # Esta si no me acuerdo para que es, pero me parece que es para mostrar la salida de los procesos
from subprocess import check_output,CalledProcessError # Esta salida hace un trabajo más bonito que Popen
from django.contrib.auth.decorators import login_required
import demoapp.models
#from demoapp.models import MediaAudio

# Implementar otra función para que haga lo mismo en archivos remotos
# @login_required(login_url='/login')
@task(name="buscar audios carpetas")
def buscar_audios_local(folder, filetype):
    matches = []
    for root, dirnames, filenames in os.walk(folder):
      for filename in fnmatch.filter(filenames, '*.'+filetype):
        matches.append(os.path.join(root, filename))
    return (matches, len(matches))

@task(name="Validar archivo con ffmpeg")
def ff_probe(file):
    
    try:
        ffprobe_dict=check_output(['ffprobe', '-print_format',  'json', '-show_entries', 'format : stream',  file,])
        ffprobe_dict=literal_eval(ffprobe_dict.decode('utf8').replace('\n',''))
        ffprobe_dict['md5']= check_output(['md5sum',  file, ]).decode('utf8').replace('\n','')[:32]
    except CalledProcessError:
        pass

    return ffprobe_dict

@task(name="Duraccion en segundos archivo")
def duracion_segundos(file):
    command = 'ffprobe -v error -show_entries format=duration\
 -of default=noprint_wrappers=1:nokey=1 ' +file
    args = split(command)
    return(float(check_output(args).decode('utf8').replace('\n','')))

@task(name="Construir metadatos")
def metadata(file):
    archivo = os.path.normpath(file)
    metadatosTemporal = ff_probe.delay(archivo)
    metadatos = metadatosTemporal.get()
    audio_item= demoapp.models.MediaAudio()
    audio_item.nombreArchivo=os.path.basename(archivo)
    audio_item.ubicacionArchivo=os.path.dirname(archivo)
    audio_item.md5=metadatos['md5']
    audio_item.tamanoArchivo=os.path.getsize(archivo)
    audio_item.nombre_del_codec=metadatos['streams'][0]['codec_name']
    audio_item.nombre_largo_del_codec=metadatos['streams'][0]['codec_long_name']
    audio_item.base_temporal_del_codec=metadatos['streams'][0]['codec_time_base']
    audio_item.formato_de_muestreo=metadatos['streams'][0]['sample_fmt']
    audio_item.frecuencia_de_muestreo=metadatos['streams'][0]['sample_rate']
    audio_item.canales=metadatos['streams'][0]['channels']
    audio_item.tasa_de_bits = metadatos['streams'][0]['bit_rate']
    #audio_item.bits_por_muestra_en_bruto = metadatos['streams'][0]['bits_per_sample']
    audio_item.muestras = metadatos['streams'][0]['duration_ts']
    audio_item.duracion = metadatos['streams'][0]['duration']
    if format in metadatos:
        audio_item.ieng = metadatos['format']['tags']['IENG']
        audio_item.encoder_software = metadatos['format']['tags']['encoder']
        audio_item.fecha_digitalizacion = metadatos['format']['tags']['date']
    return audio_item






