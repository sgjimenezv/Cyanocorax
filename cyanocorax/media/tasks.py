from __future__ import absolute_import

from celery import shared_task
from celery.decorators import task

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def add(x, y):
    logger.info("se a sumado jejej :P ")
    return x + y


@task(name="multiplicar")
def mul(x, y):
    logger.info("se ha multiplicado")
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

@task(name="conversion de audio")
def conversionAduio(file):
    pass




from subprocess import Popen, PIPE, TimeoutExpired
from shlex import split
from django.http import StreamingHttpResponse
from django.conf import settings
@task(name="Audio streamer response OGG2")
class OggAudioStreamer(object):

    def __init__(self, archivo):
        self.archivo=archivo

    def read(self, **kwargs):
        command = 'ffmpeg -i "{0}" -ac 1 -ar 22050 -acodec libvorbis -f ogg -'.format(self.archivo)
        args = split(command)
        print(args)
        print(command)
        response = Popen(args, stdout=PIPE, stderr=PIPE, bufsize=8192, universal_newlines=False)
        response_iterator = iter(response.stdout.readline, b"")

        for resp in response_iterator:
            yield resp

@task(name="Audio streamer response OGG")
def ogg_stream_response(request,ruta):
    rutaFinal = "%s/%s" %(settings.MEDIA_ROOT, ruta)
    print(rutaFinal)
    #data0 = OggAudioStreamer.delay((rutaFinal),)
    #data = data0.get() 
    data = OggAudioStreamer(rutaFinal)
    stream = StreamingHttpResponse(data.read(),  content_type='audio/ogg')
    return stream


def convertirAudio(ruta,formato):
    pass
    



