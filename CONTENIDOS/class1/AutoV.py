from vehiculo import Vehiculo


class AutoVehivulo(Vehiculo):
    def __init__(self, marca, modelo,numPuertas, anio):
        super().__init__(marca, modelo, anio)
        self.numPuertas = numPuertas
    
    def descripcion(self):
        return f'MARCA: {self.marca} \nMODELO {self.modelo} \nNumero Puertas {self.numPuertas}  \nAÑO {self.anio} \n'
    