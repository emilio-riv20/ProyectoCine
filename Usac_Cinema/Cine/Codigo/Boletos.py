
ListaBoletos = []

class DatosBoletos:

    def AgregarCompra(self, id, boletos, sala, asientos, fecha, hora, nombre, nit, direccion, metodo, total):
        boleto = {'id': id,'boletos': boletos, 'sala': sala,'asientos': asientos,'fecha': fecha, 'hora': hora, 'nombre': nombre, 'nit': nit, 'direccion': direccion, 'metodo': metodo, 'total': total}
        for i in range(int (boletos)):
            ListaBoletos.append(boleto)
            i += 1

    def Eliminar(self, nombre):
        for boleto in ListaBoletos:
            if boleto['nombre'] == nombre:
                ListaBoletos.remove(boleto)

    def __iter__(self):
        self.indice = 0
        return self

    def __next__(self):
        if self.indice < len(ListaBoletos):
            boleto = ListaBoletos[self.indice]
            self.indice += 1
            return boleto
        else:
            raise StopIteration

Boletos = DatosBoletos()