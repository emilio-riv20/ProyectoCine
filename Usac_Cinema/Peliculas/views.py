from django.shortcuts import render
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

def EliminarPeliculas(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        comprobar = ListadoPelis.ComprobarID(id)
        
        if comprobar ==  True:
            ListadoPelis.Eliminar(id)
            messages.success(request, 'Película Eliminada')
        else:
            messages.error(request, 'Película No Econtrada')
    return render(request, 'EliminarPeliculas.html')

def ModificarPeliculas(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        comprobar = ListadoPelis.ComprobarID(id)

        if comprobar == True:
            nuevoID = request.POST.get('nuevoID')
            nuevoNombre = request.POST.get('nuevoNombre')
            nuevaFecha = request.POST.get('nuevaFecha')
            nuevaHora = request.POST.get('nuevaHora')
            nuevaCategoria = request.POST.get('nuevaCategoria')
            nuevoLink = request.POST.get('nuevoLink')
            ListadoPelis.Modificar(id, nuevoID, nuevoNombre, nuevaFecha, nuevaHora, nuevaCategoria, nuevoLink)
            messages.success(request, 'Película Modificada')
        else:
            messages.error(request, 'Película No Encontrada')
    return render(request, 'ModificarPeliculas.html')

def ListaPeliculas(request):
    return render(request, 'ListaPeliculas.html', {'NodoPelis': ListadoPelis})

def ListaPeliculasMenu(request):
    return render(request, 'ListaPeliculasMenu.html', {'NodoPelis': ListadoPelis})

def ListaPeliculasMenuCliente(request):
    return render(request, 'ListaPeliculasMenuCliente.html', {'NodoPelis': ListadoPelis})

def Cargar_xmlP(request):
    if request.method == 'POST':
        ListadoPelis.Cargar_xmlP(1)
    return render(request, 'ListaPeliculas.html', {'NodoPelis': ListadoPelis})
