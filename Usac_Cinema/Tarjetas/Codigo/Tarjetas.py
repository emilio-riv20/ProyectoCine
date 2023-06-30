from Tarjetas.Codigo.NodoTarjetas import NodoTarjetas
import xml.etree.ElementTree as ET
import requests

class Tarjetas:
    def __init__(self):
        self.cabeza =  None

    def __iter__(self):
        actual = self.cabeza
        while actual:
            yield actual
            actual = actual.siguiente


    def Agregar(self, tipo, numero, titular, fecha):
        nuevo = NodoTarjetas(tipo, numero, titular, fecha)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual =actual.siguiente
            actual.siguiente = nuevo
            nuevo.anterior = actual

    def ComprobarNumero(self, numero):
        if self.cabeza is None:
            return False

        actual = self.cabeza
        while actual:
            if actual.numero == numero:
                return True
            actual = actual.siguiente
        return False

    def Eliminar(self, numero):
        actual = self.cabeza

        if actual is None:
            return
        elif actual.numero == numero:
            self.cabeza = actual.siguiente
            return
        actual = self.cabeza

        while actual is not None:
            if actual.numero == numero:
                break
            actual = actual.siguiente
        if actual is None:
            return
        actual.anterior = actual.siguiente

    def Modificar(self, numero, tipoNuevo, numeroNuevo, titularNuevo, fechaNueva):
        actual = self.cabeza
        if actual is None:
            print("Lista vacia")
            return
        while actual:
            if actual.numero == numero:
                actual.tipo = tipoNuevo
                actual.numero = numeroNuevo
                actual.titular = titularNuevo
                actual.fecha = fechaNueva
                return
            actual = actual.siguiente

    def Cargar_xmlT(self, operacion):
        
        tree = ET.parse('Tarjetas.xml')
        root = tree.getroot()

        for indice, tarjeta in enumerate(root.findall('tarjeta')):
            tipo = tarjeta.find('tipo').text
            numero = tarjeta.find('numero').text
            titular = tarjeta.find('titular').text
            fecha = tarjeta.find('fecha').text
            
            if operacion == 1:
                comprobar = self.ComprobarNumero(numero)
                if comprobar == False:
                    self.Agregar(tipo, numero, titular, fecha)
                else:
                    print("Fallo")

ListaTarjetas = Tarjetas()