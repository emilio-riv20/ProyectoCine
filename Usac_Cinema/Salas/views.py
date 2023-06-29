from django.shortcuts import render
from Salas.Codigo.Salas import ListaSalas
from django.contrib import messages
import requests

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

def Cargar_xmlS(request):
    if request.method == 'POST':
        ListaSalas.Cargar_xmlS(1)

        response = requests.get('http://localhost:5007/getSalas')
        APIsalas = response.json()

        for sala in APIsalas['sala']:
            numero = sala['numero']
            asientos = sala['asientos']
            comprobar = ListaSalas.Comprobar(numero)
            if comprobar == False:
                ListaSalas.agregar(numero, asientos)
            else:
                print("Sala Existente")

    return render(request, 'MostrarSalas.html', {'Nodo': ListaSalas})
