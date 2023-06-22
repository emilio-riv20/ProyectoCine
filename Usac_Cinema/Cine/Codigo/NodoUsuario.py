class Nodo:
    def __init__(self, nombre, apellido, telefono, correo, contraseña, rol):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contraseña = contraseña
        self.rol = rol
        self.telefono = telefono
        self.siguiente = None