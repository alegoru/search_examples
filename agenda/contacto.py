class Contacto:
    nombre:str
    telefono:str

    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    def __repr__(self):
        return f"{self.nombre} - {self.telefono}"