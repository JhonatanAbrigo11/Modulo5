from datetime import datetime
nombre_paciente= []
edad_pacientes = []
def agregar_nombre (nombre,apellido):
    nombre_paciente.append((nombre,apellido))
    
def agregar_edad (anio_nacimiento) :
    anio_actual = datetime.now().year
    edad = anio_actual - anio_nacimiento
    edad_pacientes.append(edad)

def obtener_mayor_menor():
    max_edad = max(edad_pacientes)
    min_edad = min(edad_pacientes)
    
    index_mayor = edad_pacientes.index(max_edad)
    index_menor = edad_pacientes.index(min_edad)
    
    print(f"El paciente mayor es {nombre_paciente[index_mayor]} con {max_edad} años.")
    print(f"El paciente menor es {nombre_paciente[index_menor]} con {min_edad} años.")
def imprimir ():
    print (nombre_paciente + edad_pacientes)