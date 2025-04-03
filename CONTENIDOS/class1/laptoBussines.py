from lapto import Laptop
import random
class Lapto_Business (Laptop) :
    def __init__(self, marca, procesador,espacioDisco, duracion_bateria, memoria, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.espacioDisco = espacioDisco
        self.duracion_bateria = duracion_bateria
        
    def realizar_diagnostico_sistema(self):
        resultadoDiagnostico = super().realizar_diagnostico_sistema()
        resultadoRed = self.verificar_conectividad_red()
        resultadoDiagnostico ['VERIFICAR CONECTIVIDAD RED: ']= resultadoRed
        return resultadoDiagnostico
    def verificar_conectividad_red (self) :
        resultados = {}
        resultadoRandomico = random.choice([True,False]) 
        if resultadoRandomico == True :
            resultados = 'Disponibilidad de WIFI'
        else : 
            resultados = 'Acceso a servidores empresialares'
            resultados = 'Latencia : 112304'
        return resultados   
    pass