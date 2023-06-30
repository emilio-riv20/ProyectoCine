from django.shortcuts import render
from Tarjetas.Codigo.Tarjetas import ListaTarjetas
from django.contrib import messages
import requests

# Create your views here.
def AgregarTarjeta(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        numero = request.POST.get('numero')
        titular = request.POST.get('titular')
        fecha = request.POST.get('fecha')

        comprobar = ListaTarjetas.ComprobarNumero(numero)
        if comprobar == False:
            ListaTarjetas.Agregar(tipo, numero, titular, fecha)
            messages.success(request, 'Tarjeta registrada con exito')
        else:
            messages.error(request, 'Tarjeta existente')
    return render(request, 'AgregarTarjeta.html')

def EliminarTarjeta(request):
    if request.method == 'POST':
        numero = request.POST.get('numero')
        comprobar = ListaTarjetas.ComprobarNumero(numero)
        
        if comprobar ==  True:
            ListaTarjetas.Eliminar(numero)
            messages.success(request, 'Tarjeta Eliminada')
        else:
            messages.error(request, 'Tarjeta No Econtrada')
    return render(request, 'EliminarTarjeta.html')

def ModificarTarjeta(request):
    if request.method == 'POST':
        numero = request.POST.get('numero')
        comprobar = ListaTarjetas.ComprobarNumero(numero)

        if comprobar == True:
            nuevoTipo = request.POST.get('nuevoTipo')
            nuevoNumero = request.POST.get('nuevoNumero')
            nuevoTitular = request.POST.get('nuevoTitular')
            nuevaFecha = request.POST.get('nuevaFecha')

            comprobarSalaNueva = ListaTarjetas.ComprobarNumero(nuevoNumero)

            if comprobarSalaNueva == False:
                ListaTarjetas.Modificar(numero, nuevoTipo, nuevoNumero, nuevoTitular, nuevaFecha)
                messages.success(request, 'Tarjeta Modificado')
            else:
                messages.error(request, 'Número en uso')
        else:
            messages.error(request, 'Tarjeta No Encontrada')
    return render(request, 'ModificarTarjeta.html')

def MostrarTarjetas(request):
    return render(request, 'MostrarTarjetas.html', {'Nodo': ListaTarjetas})

def Cargar_xmlT(request):
    if request.method == 'POST':
        ListaTarjetas.Cargar_xmlT(1)

        response = requests.get('http://localhost:5007/getTarjeta')
        APItarjetas = response.json()

        for tarjeta in APItarjetas['tarjeta']:
            tipo = tarjeta['tipo']
            numero = tarjeta['numero']
            titular = tarjeta['titular']
            fecha = tarjeta['fecha']
            comprobar = ListaTarjetas.ComprobarNumero(numero)
            if comprobar == False:
                ListaTarjetas.Agregar(tipo, numero, titular, fecha)
            else:
                print("Tarjeta Existente")

    return render(request, 'MostrarTarjetas.html', {'Nodo': ListaTarjetas})
