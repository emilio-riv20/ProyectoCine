from django.shortcuts import render
from Salas.Codigo.Salas import ListaSalas
from django.contrib import messages

# Create your views here.
def RegistrarSalas(request):
    if request.method == 'POST':
        numero = request.POST.get('numero')
        asientos = request.POST.get('asientos')

        comprobar = ListaSalas.Comprobar(numero)
        if comprobar == False:
            ListaSalas.agregar(numero, asientos)
            messages.success(request, 'Sala registrada con exito')
        else:
            messages.error(request, 'Sala existente')
    return render(request, 'RegistrarSalas.html')

def EliminarSalas(request):
    if request.method == 'POST':
        numero = request.POST.get('numero')
        comprobar = ListaSalas.Comprobar(numero)
        
        if comprobar ==  True:
            ListaSalas.Eliminar(numero)
            messages.success(request, 'Sala Eliminada')
        else:
            messages.error(request, 'Sala No Econtrada')
    return render(request, 'EliminarSalas.html')

def ModificarSalas(request):
    if request.method == 'POST':
        numero = request.POST.get('numero')
        comprobar = ListaSalas.Comprobar(numero)

        if comprobar == True:
            nuevoNumero = request.POST.get('nuevoNumero')
            nuevosAsientos = request.POST.get('nuevosAsientos')
            ListaSalas.Modificar(numero, nuevoNumero, nuevosAsientos)
            messages.success(request, 'Sala Modificado')
        else:
            messages.error(request, 'Sala No Encontrada')
    return render(request, 'ModificarSalas.html')

def MostrarSalas(request):
    return render(request, 'MostrarSalas.html', {'Nodo': ListaSalas})