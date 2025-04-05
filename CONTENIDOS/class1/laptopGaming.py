from lapto import Laptop


class Laptop_Gaming(Laptop):
    def __init__(self, marca, procesador, memoria, tarjet_graf, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.tarjet_graf = tarjet_graf
        
    def __str__(self):
          return f'Marca {self.marca} \n Procesador {self.procesador} \n Memoria {self.memoria} \n Targera Grafica {self.tarjet_graf} \n Costo {self.costo} \n Impuesto {self.impuesto} \n'
      
    def realizar_diagnostico_sistema(self):
        resultadoDiagnostico = super().realizar_diagnostico_sistema()
        resultadoJuego = self.realizar_diagnostico_juegos()
        resultadoDiagnostico ['Resultado juegos'] = resultadoJuego
        return resultadoDiagnostico
            
    def realizar_diagnostico_juegos(self):
        juegos = ['FORTNITE', 'COD', 'GTA']
        resultados = {}
        fps_base = 30

        for juego in juegos:
            if 'RTX' in self.tarjet_graf:
                    fps = fps_base * 3
            elif 'GTX' in self.tarjet_graf:
                    fps = fps_base * 2
            else:
                    fps = fps_base
                    
            resultados[juego] = f'{fps} FPS'

        return resultados
    def realizar_informe_uso(self):
          informe =  super().realizar_informe_uso()
          informe.update({
               'Tipo' : 'Generico ',
               'Uso Recomendado ': 'Juegos de video',
               'Horas de uso ': 5,
               'Recomendaciones de software': ['Antivirus','VPN']
          })
          return informe
    pass 

