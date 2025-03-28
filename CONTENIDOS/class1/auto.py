

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
            

auto_Jhonatan = auto('CHEVROLET','HI-RIDE','2025',10000)
auto.mostrarInformacion(auto_Jhonatan)
auto.actualizar_kilometraje(auto_Jhonatan,11000)
auto.realizar_viaje(auto_Jhonatan,200)
auto.estado_auto(auto_Jhonatan)

