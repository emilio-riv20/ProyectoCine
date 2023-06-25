from Peliculas.Codigo.NodoPelis import Informacion
import xml.etree.ElementTree as ET 

class Listado():

    def __init__(self):
        self.cabeza = None

    def __iter__(self):
        actual = self.cabeza

        if self.cabeza is None:
            return iter([])

        while actual:
            yield actual 
            actual = actual.siguiente
            if actual == self.cabeza:
                break

    def Agregar(self, ID, nombre, fecha, hora, categoria, link):
        pelicula = Informacion(ID, nombre, fecha, hora, categoria, link)
        
        if self.cabeza is None:
            self.cabeza = pelicula
            self.cabeza.siguiente = self.cabeza
            self.cabeza.anterior = self.cabeza
        else:
            ultimo = self.cabeza.anterior

            pelicula.siguiente = self.cabeza
            pelicula.anterior = ultimo
            
            self.cabeza.anterior = pelicula
            ultimo.siguiente = pelicula

    def ImprimirInformacion(self):
        if self.cabeza is None:
            return
        actual = self.cabeza
        while True:
                print("------Información-----")
                print("ID:",actual.ID)
                print("Nombre:",actual.nombre)
                print("Fecha de función:",actual.fecha)
                print("Hora de función:",actual.hora)
                actual = actual.siguiente
                if actual == self.cabeza:
                    break

    def ImprimirPeli(self, id):
        actual =self.cabeza
        while actual:
            if actual.ID == id:
                print("------------------")
                print("ID:",actual.ID)
                print("Nombre:",actual.nombre)
                print("Fecha de función:",actual.fecha)
                print("Hora de función:",actual.hora)
                print("-----------------")
            actual = actual.siguiente
            if actual == self.cabeza:
                break

    def imprimir(self):
        if self.cabeza is None:
            return
        actual = self.cabeza
        while True:
            print("ID: ",actual.ID)
            print("Nombre:",actual.nombre)
            print("-----------------------")
            actual = actual.siguiente
            if actual == self.cabeza:
                break
    
    def ComprobarID(self, id):
        actual = self.cabeza
        while actual:
            if actual.ID == id:
                return True
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        return False    

    def Eliminar(self, ID):
        if self.cabeza is None:
            return

        if self.cabeza.ID == ID:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = self.cabeza.siguiente
            self.cabeza = self.cabeza.siguiente
        else:
            actual = self.cabeza
            previo = None
            while actual.siguiente != self.cabeza:
                previo = actual
                actual = actual.siguiente
                if actual.ID == ID:
                    previo.siguiente = actual.siguiente
                    break

    def Modificar(self, ID, nuevoID, nuevoNombre, nuevaFecha, nuevaHora, nuevCategoria, nuevoLink):
        actual = self.cabeza
        while True:
            if actual.ID == ID:
                actual.ID = nuevoID
                actual.nombre = nuevoNombre
                actual.fecha = nuevaFecha
                actual.hora = nuevaHora
                actual.categoria = nuevCategoria
                actual.link = nuevoLink
                break
            actual = actual.siguiente
            if actual == self.cabeza:
                break

    def Cargar_xmlP(self, operacion):
        
        tree = ET.parse('Peliculas.xml')
        root = tree.getroot()

        for indice, pelicula in enumerate(root.findall('pelicula')):
            id = pelicula.find('id').text
            nombre = pelicula.find('nombre').text
            fecha = pelicula.find('fecha').text
            hora = pelicula.find('hora').text
            categoria = pelicula.find('categoria').text
            link = pelicula.find('link').text
            
            if operacion == 1:
                comprobar = self.ComprobarID(id)
                if comprobar == False:
                    self.Agregar(id, nombre, fecha, hora, categoria, link)
                else:
                    print("Fallo")

ListadoPelis = Listado()