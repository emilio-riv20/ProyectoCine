from django.contrib import messages
from django.shortcuts import render, redirect
from Cine.Codigo.Registrar_Usuario import AñadirUsuario
from Cine.Codigo.Boletos import Boletos
from Peliculas.Codigo.Listado_Pelis import ListadoPelis
from Salas.Codigo.Salas import ListaSalas

AñadirUsuario.Agregar('Emilio', 'Rivera', '58725886', 'lemilioriveray@gmail.com', '123456', 'Administrador')

# Create your views here.
def Menu(request):
    return render(request, 'Menu.html')

def RegistrarUsuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contraseña')

        comprobar = AñadirUsuario.ComprobarCorreo(correo)
        if comprobar == False:
            AñadirUsuario.Agregar(nombre, apellido, telefono, correo , contraseña , 'Cliente')
            messages.success(request, 'Usuario registrado con exito')
        else:
            messages.error(request, 'Usuario existente')
    return render(request, 'RegistrarUsuario.html')

def IniciarSesion(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contraseña')
        comprobar = AñadirUsuario.ComprobarDatos(correo, contraseña)
        comprobarRol = AñadirUsuario.ComprobarRol(correo)
        if comprobar == True and comprobarRol =='Cliente':
            return redirect('MenuCliente')
        
        elif comprobar == True and comprobarRol == 'Administrador':
            return redirect ('MenuAdmin')
        else:
            messages.error(request, 'Usuario no Existente')
    return render(request, 'IniciarSesion.html')
        
def MenuCliente(request):
    return render(request, 'MenuCliente.html')

def Compra(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        boletos = request.POST.get('boletos')
        sala = request.POST.get('sala')
        asientos = request.POST.get('asientos')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        nombre = request.POST.get('nombre')
        nit = request.POST.get('nit')
        direccion = request.POST.get('direccion')
        metodo = request.POST.get('metodo')

        comprobarId = ListadoPelis.ComprobarID(id)
        comprobarSala = ListaSalas.Comprobar(sala)

        if comprobarId == True and comprobarSala == True:
            if int (boletos) <= 0:
                messages.error(request, 'La cantidad de Boletos debe ser mayor a 0')
            else:
                if nit != 0:
                    total = int (boletos) * 42
                    Boletos.AgregarCompra(id, boletos, sala, asientos, fecha, hora, nombre, nit, direccion, metodo, total)
                    messages.success(request, 'Boleto añadido')
                elif nit == 0:
                    total = int (boletos) * 42
                    Boletos.AgregarCompra(id, boletos, sala, asientos, fecha, hora, nombre, nit, 'CF', metodo, total)
                    messages.success(request, 'Boleto añadido')
        else:
            messages.error(request, 'Id o Sala no existentes')

    return render(request, 'Compra.html')

def ListaBoletos(request):
    return render(request, 'ListaBoletos.html', {'Boletos': Boletos})