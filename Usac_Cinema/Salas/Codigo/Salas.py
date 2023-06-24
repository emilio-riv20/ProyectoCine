from Salas.Codigo.NodoSalas import NodoSalas
import xml.etree.ElementTree as ET

class Salas:
    def __init__(self):
        self.cabeza =  None

    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual
            actual = actual.siguiente


    def agregar(self, N_sala, N_asiento):
        nuevo = NodoSalas(N_sala, N_asiento)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual =actual.siguiente
            actual.siguiente = nuevo
            nuevo.anterior = actual

    def Comprobar(self, N_sala):
        if self.cabeza is None:
            return False

        actual = self.cabeza
        while actual:
            if actual.N_sala == N_sala:
                return True
            actual = actual.siguiente
        return False

    def imprimir(self):
            actual = self.cabeza
            while actual:
                print("Número de sala: ",actual.N_sala)
                print("Número de asientos: ",actual.N_asiento)
                print("--------------------------")
                actual = actual.siguiente

    def Eliminar(self, N_sala):
        actual = self.cabeza

        if actual is None:
            return
        elif actual.N_sala == N_sala:
            self.cabeza = actual.siguiente
            return
        actual = self.cabeza

        while actual is not None:
            if actual.N_sala == N_sala:
                break
            actual = actual.siguiente
        if actual is None:
            return
        actual.anterior = actual.siguiente

    def Modificar(self, N_sala, NuevaSala, NuevosAsientos):
        actual = self.cabeza
        if actual is None:
            print("Lista vacia")
            return
        while actual:
            if actual.N_sala == N_sala:
                actual.N_sala = NuevaSala
                actual.N_asiento = NuevosAsientos
                return
            actual = actual.siguiente
        print("Sala no encontrada")

    def GuardarXML(self, Nombre):
        root = ET.Element("Salas")
        actual = self.cabeza
        while actual:
            pelicula = ET.SubElement(root, "Salas")
            N_sala = ET.SubElement(pelicula, "Numero")
            N_asientos = ET.SubElement(pelicula, "Asientos") 
            N_sala.text = actual.N_sala
            N_asientos.text = actual.N_asiento
            actual = actual.siguiente
            ET.SubElement(root, "\n")

            if actual == self.cabeza:
                break

        arbol = ET.ElementTree(root)
        arbol.write(Nombre)

ListaSalas = Salas()