from django.contrib import admin
from LibreriaWeb.Apps.GestionLibros.models import *
# Register your models here.

admin.site.register(Autor)
admin.site.register(Idioma)
admin.site.register(Libro)
admin.site.register(Genero)
admin.site.register(Venta)