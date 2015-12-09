from django.contrib import admin
from .models import Menu, MenuItem

# Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('texto', )


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('texto', 'padre', 'clase', 'peso', 'destino')
