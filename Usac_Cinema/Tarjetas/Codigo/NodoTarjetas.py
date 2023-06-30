class NodoTarjetas:
    def __init__(self, tipo, numero, titular, fecha):
        self.tipo = tipo
        self.numero = numero
        self.titular = titular
        self.fecha = fecha
        self.siguiente = None
        self.anterior = None