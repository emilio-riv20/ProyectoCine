import xml.etree.ElementTree as ET
from Cine.Codigo.NodoUsuario import Nodo

class ListaUsuarios:

    def __init__(self):
        self.cabeza = None

    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual
            actual = actual.siguiente

    def Agregar(self, nombre, apellido, telefono, correo, contraseña, rol):
        nuevo = Nodo(nombre, apellido, telefono, correo, contraseña, rol)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo
        print("Usuario agregado")

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print("Correo:", actual.correo, "Contraseña:", actual.contraseña)
            actual = actual.siguiente

    def ComprobarDatos(self, correo, contraseña):
        actual = self.cabeza
        while actual:
            if actual.correo == correo and actual.contraseña == contraseña:
                return True
            actual = actual.siguiente
        return False
    
    def ComprobarCorreo(self, correo):
        actual = self.cabeza
        while actual:
            if actual.correo == correo:
                return True
            actual = actual.siguiente
        return False
    

    def ComprobarRol(self, correo):
        actual = self.cabeza
        while actual:
            if actual.correo == correo:
                return actual.rol
            actual = actual.siguiente
        return None
    
    def ImprimirTodo(self):
        actual = self.cabeza
        while actual:
            print("------------------------------")
            print("Nombre:",actual.nombre)
            print("Apellido:",actual.apellido)
            print("Teléfono:",actual.telefono)
            print("Correo:",actual.correo)
            print("Rol:",actual.rol)
            print("------------------------------")
            actual = actual.siguiente

    def Modificar(self, correo, nuevo_nombre, nuevo_apellido, nuevo_telefono, nuevo_correo, nueva_contra, nuevo_rol):
        actual = self.cabeza
        while actual:
            if actual.correo == correo:
                actual.nombre = nuevo_nombre
                actual.apellido = nuevo_apellido
                actual.telefono = nuevo_telefono
                actual.correo = nuevo_correo
                actual.contraseña = nueva_contra
                actual.rol = nuevo_rol
                break
            actual = actual.siguiente

    def Eliminar(self, correo):
        actual = self.cabeza

        if actual is None:
            return
        elif actual.correo == correo:
            self.cabeza = actual.siguiente
            return
        actual = self.cabeza
        anterior = None

        while actual is not None:
            if actual.correo == correo:
                break
            anterior =actual
            actual = actual.siguiente
        if actual is None:
            return
        anterior.siguiente = actual.siguiente

    def CargarXML(self, operacion):
        
        tree = ET.parse('Usuarios.xml')
        root = tree.getroot()

        for indice, usuarios in enumerate(root.findall('usuario')):
            nombre = usuarios.find('nombre').text
            apellido = usuarios.find('apellido').text
            telefono = usuarios.find('telefono').text
            correo = usuarios.find('correo').text
            contraseña = usuarios.find('contrasena').text
            rol = usuarios.find('rol').text
            
            if operacion == 1: # agregar datos a lista
                comprobar = self.ComprobarCorreo(correo)
                if comprobar == False:
                    self.Agregar(nombre, apellido, telefono, correo, contraseña, rol)
                else:
                    print("Fallo")

AñadirUsuario = ListaUsuarios()