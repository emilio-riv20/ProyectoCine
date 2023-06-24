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

    def guardar_en_xml(self, Nombre):
        root = ET.Element("Peliculas")
        actual = self.cabeza
        while True:
            pelicula = ET.SubElement(root, "Pelicula")
            ID = ET.SubElement(pelicula, "ID")
            nombre = ET.SubElement(pelicula, "Nombre") 
            fecha = ET.SubElement(pelicula, "Fecha")
            hora = ET.SubElement(pelicula, "Hora")
            categoria = ET.SubElement(pelicula, "Categoria")
            ID.text = actual.ID
            nombre.text = actual.nombre
            fecha.text = actual.fecha
            hora.text = actual.hora
            categoria.text = actual.categoria
            actual = actual.siguiente
            ET.SubElement(root, "\n")

            if actual == self.cabeza:
                break

        arbol = ET.ElementTree(root)
        arbol.write(Nombre)

ListadoPelis = Listado()