ListaBoletos = []

class DatosBoletos:
    def AgregarCompra(self, nombre, nit, direccion, boletos, sala, asientos, total):
        for i in range (boletos):
            boleto = {'nombre': nombre,'nit': nit,'direccion': direccion,'sala': sala, 'asientos': asientos, 'total': total}
            ListaBoletos.append(boleto)
            i += 1


    def Imprimir(self, nombre, boletos):
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
                print("-------------------------")