from vehiculo import Vehiculo


class Moto (Vehiculo):
    def __init__(self, marca, modelo,tipo, anio):
        self.tipo = tipo
        super().__init__(marca, modelo, anio)
        
    def descripcion(self):
        return f'MARCA>> {self.marca} \nMODELO>> {self.modelo} \nTIPO>> {self.tipo}  \nAÑO>> {self.anio} \n'