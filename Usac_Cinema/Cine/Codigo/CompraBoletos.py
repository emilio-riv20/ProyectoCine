from Peliculas.Codigo.Listado_Pelis import ListadoPelis
from Cine.Codigo.Boletos import DatosBoletos    
Datos = DatosBoletos()

class Compra:

    def __init__(self, id, boletos, sala, asientos, fecha, hora, nombre, nit, direccion, metodo, total):
        self.id = id
        self.boletos = boletos
        self.sala = sala
        self.asientos = asientos
        self.fecha = fecha
        self.hora = hora
        self.nombre = nombre
        self.nit = nit
        self.direccion = direccion
        self.metodo = metodo
        self.total = total

    def comprar(self, id, boletos, sala, asientos, fecha, hora, nombre, nit, direccion, metodo, total):
        existe = ListadoPelis.ComprobarID(id)
        if existe == True:
            Datos.AgregarCompra(id, boletos, sala, asientos, fecha, hora, nombre, nit, direccion, metodo, total)
        else: 
            print("Película no encontrada")