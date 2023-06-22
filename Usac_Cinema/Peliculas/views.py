from django.shortcuts import render, redirect
from django.contrib import messages
from Peliculas.Codigo.Listado_Pelis import ListadoPelis

# Create your views here.
def RegistrarPeliculas(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        categoria = request.POST.get('categoria')
        link = request.POST.get('link')
        comprobar = ListadoPelis.ComprobarID(id)
        if comprobar == False:
            ListadoPelis.Agregar(id, nombre, fecha, hora , categoria, link)
            messages.success(request, 'Película registrada con exito')
        else:
            messages.error(request, 'ID existente')
    return render(request, 'RegistrarPeliculas.html')

def Lista_Peliculas(request):
    Nodo = ListadoPelis
    return render(request, 'MostrarPeliculas.html', {'Nodo': Nodo})
