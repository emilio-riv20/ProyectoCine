from django.contrib import admin

from Cine.models import Peliculas, Salas, Usuarios

admin.site.register(Usuarios)
admin.site.register(Peliculas)
admin.site.register(Salas)

