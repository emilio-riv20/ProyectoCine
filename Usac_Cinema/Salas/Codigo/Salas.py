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

    def Cargar_xmlS(self, operacion):
        
        tree = ET.parse('Salas.xml')
        root = tree.getroot()

        for indice, sala in enumerate(root.findall('sala')):
            numero = sala.find('numero').text
            asientos = sala.find('asientos').text
            
            if operacion == 1:
                comprobar = self.Comprobar(numero)
                if comprobar == False:
                    self.agregar(numero, asientos)
                else:
                    print("Fallo")

ListaSalas = Salas()