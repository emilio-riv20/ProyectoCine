from django.contrib import messages
from django.shortcuts import render, redirect
from Cine.Codigo.Registrar_Usuario import AñadirUsuario

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



