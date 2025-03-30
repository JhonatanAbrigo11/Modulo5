

class auto : 
    def __init__ (self,marca,modelo,anio,kilometraje=0):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje
        
    def mostrarInformacion (self):
        print(f'MARCA: {self.marca} MODELO: {self.modelo} AÑO: {self.modelo} KILOMETRAJE: {self.kilometraje}')
    
    def actualizar_kilometraje (self,kilometraje):
        if kilometraje > self.kilometraje:
            self.kilometraje = kilometraje
            print (f'El kilometraje a sido actualizado correctamete {self.kilometraje}')
        else:
            print ('No se puede reducir el kilometraje')
    
    def realizar_viaje (self, cantidadKilometros) :
        if cantidadKilometros > 0 : 
            self.kilometraje += cantidadKilometros
            print (f'Los kilometros han sido agregado correctamente {self.kilometraje}')
        else : 
            print ('La cantidad de kilometros debe ser positiva')
    
    def estado_auto (self):
        print (f'KILOMETRAJE : {self.kilometraje}')
        if self.kilometraje < 20000 : 
            print ('Estoy como nuevo')
        elif self.kilometraje >= 20000 and self.kilometraje < 100000:
            print ('Ya estoy usado')
        else:
            print ('Ya dejame descansar por favor !!!')
    
    @classmethod
    def crearAuto (cls):
        marca = 'TOYOTA'
        modelo = 'HILUX'
        anio = '2025'
        return cls (marca,modelo,anio)
    @staticmethod
    def compararKilometraje(carro1,carro2):
        if carro1.kilometraje == carro2.kilometraje: 
            print ('Tienen el mismo kilometraje')
        else:
            print ('NO tienen el mismo kilometraje')
    @staticmethod
    def compararMarca (carro1,carro2):
        if carro1.marca == carro2.marca:
            print('SON DE LA MISMA MARCA')
        else: 
            print('NO SON DE LA MISMA MARCA ')
            
    @staticmethod
    def agregarUnaMarca(auto1,auto2,auto3):
        if auto1.marca == 'FORD' and auto2.marca == 'FORD' and auto3.marca == 'FORD':
            print ('SE AGREGARON LOS AUTOS')
        else: 
            print ('NO SE PUEDEN AGREGAR SON DE DIFERENTES MARCAS')