Bienvenidos a la documentación de la plataforma web Cyanocorax
==============================================================

Cyanocorax es una plataforma web de código abierto para el manejo de materiales
de audio usados en investigaciones lingüísticas, desarrollada por el grupo de
Lingüística de Corpus del Instituto Caro y Cuervo.

.. figure:: Cyanocorax_yncas.jpg
   :align: center
   :alt: Cyanocorax Yncas

   Cyanocorax Yncas. Imágen tomada de Wikipedia


La paltaforma:
--------------

Cyanocorax esta basado en `Django <https://www.djangoproject.com/>`_, un entorno
de desarrollo web escrito en  `Python <https://www.python.org/>`_.

Utiliza la base de datos estructurada `MySQL <https://www.mysql.com/>`_
para tareas administrativas, la base de datos no estructurada `Mongo
<https://www.mongodb.org/>`_ para el manejo de metadatos y la base de datos en
memoria `Redis <http://redis.io/>`_ para el manejo de tareas asíncronas.

La manipulación de archivos de audio se realiza principalmente con `ffmpeg
<https://www.ffmpeg.org/>`_, una poderosa colección de herramientas libres para
manipulación de audio y video.
