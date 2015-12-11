from django import forms
from tinymce.widgets import TinyMCE


class CrearColeccion(forms.Form):

    creacion = (('locales', 'Los archivos de la colección estan en la  \
máquina local (este servidor web)'),
                ('webdav', 'Los archivos de la colección estan en una \
carpeta remota WebDav'),
                ('crear',  'Solo crear la colección, los archivos se \
agregaran después'), )

    collection_name = forms.CharField(
        label='Nombre de la colección',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Nombre de la colección',
                   'ng-model': 'datos.collection_name',
                   }
        ), )

    collection_short_name = forms.CharField(
        label='Nombre abreviado de la coleccion',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Nombre abreviado de la colección (Para \
propositos de referencia y títulos de los menus)',
                   'ng-model': 'datos.collection_short_name',
                   }
        ), )

    collection_description = forms.CharField(
        label='Descripción de la colección',
        required=True,
        widget=TinyMCE(
            attrs={'ng-model': 'datos.collection_description', }
        ), )

    collection_short_description = forms.CharField(
        label='Descripción resumida de la colección',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Descripción resumida de la colección \
para referencia rápida',
                   'ng-model': 'datos.collection_short_description'
                   }
        ), )

    collection_creation = forms.ChoiceField(
        choices=creacion,
        label='Opciones de creación',
        required=True,
        widget=forms.RadioSelect(
            attrs={
                'ng-model': 'datos.collection_creation',
                }
        ),)

    wav = forms.BooleanField(
        label='Buscar wav',
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'ng-model': 'datos.wav',
                'style' : 'display: inline-block;'
                }
            ),
        )

    mp3 = forms.BooleanField(
        label='Buscar mp3',
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'ng-model': 'datos.mp3',
                'style' : 'display: inline-block;'
                }
            ),
        )

    ogg = forms.BooleanField(
        label='Buscar ogg',
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'ng-model': 'datos.ogg',
                'style' : 'display: inline-block;'
                }
            ),
        )

    collection_location = forms.CharField(
        label='URL de la colección',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Dirección de la colección',
                'ng-model': 'datos.collection_location',
            }
        ), )

    usuario = forms.CharField(
        label='Usuario',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Usuario WebDav',
                'ng-model': 'datos.usuario',
            }
        ), )

    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña WebDav',
                'ng-model': 'datos.password',
            }
        ),)



# Cuando funcione el formulario de arriba, la idea es crear un formulario
# asociado para poner los proyectos relacionados y a este adjuntarle otro
# formulario para introducir los productos asociados al proyecto.
# Hay que modificar el formulario, pero por ahora es más urgente el buscador
# El formulario debe mostrar dos tipos de campos diferentes para el corpus
# uno si está en local y tro si está en remoto.

# class CrearProyecto(forms.Form):
# class CrearProducto(forms.Form):




# Borrar esto es de pruebas !!!!
from django.forms import ModelForm, Textarea,SelectMultiple,Form
from demoapp.models import Audio_mdl

class UploadFileForm(ModelForm):

    class Meta:
        model= Audio_mdl
        fields = ['nombre','audioFile',]

 