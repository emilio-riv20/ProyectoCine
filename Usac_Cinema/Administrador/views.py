from django.shortcuts import render
from Cine.Codigo.Registrar_Usuario import AñadirUsuario
from django.contrib import messages

# Create your views here.
def MenuAdmin(request):
    return render(request, 'MenuAdmin.html')

def RegistrarUsuarios(request):
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
    return render(request, 'RegistrarUsuarios.html')

def EliminarUsuarios(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        comprobar = AñadirUsuario.ComprobarCorreo(correo)
        
        if comprobar ==  True:
            AñadirUsuario.Eliminar(correo)
            messages.success(request, 'Usuario Eliminado')
        else:
            messages.error(request, 'Usuario No Econtrado')
    return render(request, 'EliminarUsuarios.html')

def ModificarUsuarios(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        comprobar = AñadirUsuario.ComprobarCorreo(correo)

        if comprobar == True:
            nuevoNombre = request.POST.get('nuevoNombre')
            nuevoApellido = request.POST.get('nuevoApellido')
            nuevoTelefono = request.POST.get('nuevoTelefono')
            nuevoCorreo = request.POST.get('nuevoCorreo')
            nuevaContraseña = request.POST.get('nuevaContraseña')
            nuevoRol = request.POST.get('nuevoRol')
            AñadirUsuario.Modificar(correo, nuevoNombre, nuevoApellido, nuevoTelefono, nuevoCorreo, nuevaContraseña, nuevoRol)
            messages.success(request, 'Usuario Modificado')
        else:
            messages.error(request, 'Usuario No Encontrado')
    return render(request, 'ModificarUsuarios.html')

def Lista_Usuarios(request):
    return render(request, 'MostrarUsuarios.html', {'Nodo': AñadirUsuario})