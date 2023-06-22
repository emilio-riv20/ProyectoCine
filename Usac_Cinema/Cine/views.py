from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from Cine.Codigo.Registrar_Usuario import AñadirUsuario

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
        if comprobar == True:
            return redirect('MenuCliente')
        else:
            return HttpResponse ("Usuario No Existente")
    return render(request, 'IniciarSesion.html')
        
def MenuCliente(request):
    return render(request, 'MenuCliente.html')

def Lista_Usuarios(request):
    Nodo = AñadirUsuario
    return render(request, 'MostrarUsuarios.html', {'Nodo': Nodo})

