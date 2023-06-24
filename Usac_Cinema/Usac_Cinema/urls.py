"""
URL configuration for Usac_Cinema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Cine.views import Menu, RegistrarUsuario, IniciarSesion, MenuCliente
from Peliculas.views import RegistrarPeliculas, EliminarPeliculas, ModificarPeliculas, ListaPeliculas
from Administrador.views import  MenuAdmin, RegistrarUsuarios, EliminarUsuarios, ModificarUsuarios, Lista_Usuarios

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Menu, name = 'Menu'),
    path('RegistrarUsuario', RegistrarUsuario, name= 'RegistrarUsuario'),
    path('MenuAdmin/RegistrarPeliculas', RegistrarPeliculas, name = 'RegistrarPeliculas'),
    path('IniciarSesion', IniciarSesion, name = 'IniciarSesion'),
    path('Menu/Cliente/', MenuCliente, name = 'MenuCliente'),
    
    path('MenuAdmin/', MenuAdmin, name = 'MenuAdmin'),
    path('MenuAdmin/EliminarPeliculas', EliminarPeliculas, name='EliminarPeliculas'),
    path('MenuAdmin/ModificarPeliculas', ModificarPeliculas, name = 'ModificarPeliculas'),
    path('MenuAdmin/Listado', ListaPeliculas, name = 'ListaPeliculas'),

    path('MenuAdmin/RegistrarUsuarios', RegistrarUsuarios, name = 'RegistrarUsuarios'),
    path('MenuAdmin/EliminarUsuarios', EliminarUsuarios, name = 'EliminarUsuarios'),
    path('MenuAdmin/ModificarUsuarios', ModificarUsuarios, name = 'ModificarUsuarios'),
    path('MenuAdmin/MostrarUsuarios', Lista_Usuarios, name = 'Lista_Usuarios') 
]
