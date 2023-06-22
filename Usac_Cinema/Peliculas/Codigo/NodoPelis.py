class Informacion:
    def __init__(self, ID, nombre, fecha, hora, categoria, link):
        self.ID = ID
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora
        self.categoria = categoria
        self.link = link
        self.siguiente = None
        self.anterior = None