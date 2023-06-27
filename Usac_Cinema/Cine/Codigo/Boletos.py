
ListaBoletos = []

class DatosBoletos:

    def AgregarCompra(self, id, boletos, sala, asientos, fecha, hora, nombre, nit, direccion, metodo, total):
        boleto = {'id': id,'boletos': boletos, 'sala': sala,'asientos': asientos,'fecha': fecha, 'hora': hora, 'nombre': nombre, 'nit': nit, 'direccion': direccion, 'metodo': metodo, 'total': total}
        ListaBoletos.append(boleto)

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


    """def Imprimir(self, nombre, boletos):
        if len(ListaBoletos) > 0:
            for boleto in ListaBoletos:
                for i in range(boletos):
                    if boleto['nombre'] == nombre:
                        print("-----#USACIPC2_202004712_",i+1,"-----")
                        print("Nombre:",boleto['nombre'])
                        print("NIT:",boleto['nit'])
                        print("Dirección:",boleto['direccion'])
                        print("Sala:",boleto['sala'])
                        print("Asientos:",boleto['asientos'])
                        print("Total:",boleto['total'])
                        print("-------------------------")
                    i += 1
                break
        else:
            print("Lista vacia")

    def ImprimirPorNombre(self, nombre):
        for boleto in ListaBoletos:
            if boleto['nombre'] == nombre:
                print("-----#USACIPC2_202004712-----")
                print("Nombre:",boleto['nombre'])
                print("NIT:",boleto['nit'])
                print("Dirección:",boleto['direccion'])
                print("Sala:",boleto['sala'])
                print("Asientos:",boleto['asientos'])
                print("Total:",boleto['total'])
                print("-------------------------")"""

Boletos = DatosBoletos()