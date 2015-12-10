from django.test import TestCase
from productos.models import Producto

# Create your tests here.
Producto.objects.create(
    titulo = "Atlas Lingüístico-Etnográfico de Colombia",
    tipo = "Libro",
    descripcion = "Atlas en 6 tomos y un manual"
#    referencia = "Floréz, L., Montes Giraldo, J. J., \
#    Mora Monroy, S. C., Rodríguez de Montes, M. L., \
#    Figuero Lorza, J., y Lozano Ramírez, M. \
#    (1982). Atlas lingüístico -Etnográfico de Colombia. ALEC. \
#    Bogotá: Instituto Caro y Cuervo."
#    enlace = "http://www.lenguasdecolombia.gov.co/content/atlas-lingüístico-etnográfico-de-colombia-alec"
)
