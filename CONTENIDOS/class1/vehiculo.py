

class Vehiculo : 
    def __init__(self,marca,modelo,anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        
    def descripcion(self):
        return f'MARCA: {self.marca} \nMODELO {self.modelo} \nAÑO {self.anio}'
    
        pass