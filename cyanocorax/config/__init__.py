'''
Configuración de la plataforma
==============================

La configuración del y el desarrollo general de la plataforma se ralizaron siguiendo
las pautas de diseño y buenas prácticas contenidas en el libro `Two Scoops of
Django, Best Practices For Django 1.8
<http://www.amazon.com/Two-Scoops-Django-Best-Practices/dp/0981467342>`_

La carpeta de configuración del proyecto producida por el comando ``django-admin
startproject <nombre_del_proyecto>``  se llamaba  *nombre_del_proyecto*, en este
caso **cyanocorax**. Este nombre modificó para que pase a llamarse config, que está
más acorde a su contenido.

Dentro de la carpeta config se generó la carpeta setting que contiene tres archivos
de configuración:

  * el archivo **base.py** del que heredan los demás,
  * el archivo **local.py**  para las pruebas en la máquina de desarrollo
  * el archivo **production.py**  para ajustar los criterios de seguridad al entorno de producción

También hay un archivo json con los datos de conección a las bases de
datos y la SECRET_KEY usada por Django como recurso criptográfico.

La estructura completa de la carpeta config sería:


+--------+-----------+-----------------+
| config                               |
+--------+-----------+-----------------+
|        | settings                    |
+        +-----------+-----------------+
|        |           | base.py         |
+        +           +-----------------+
|        |           | local.py        |
+        +           +-----------------+
|        |           | production.py   |
+        +           +-----------------+
|        |           | secrets.py      |
+        +-----------+-----------------+
|        | urls.py                     |
+        +-----------+-----------------+
|        | wsgi.py                     |
+--------+-----------+-----------------+



Para que la carpeta config fuera interpretada por Django como carpeta de configuración
se modificaron los archivos manage.py y wsgi.py para declarar la nueva ruta:

línea original : ``os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cyanocorax.settings")``

línea modificada para local: ``os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")``

línea modificada para produccion: ``os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")``

'''



from __future__ import absolute_import

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ['celery_app']
