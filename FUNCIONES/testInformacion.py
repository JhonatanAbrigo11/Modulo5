import reto5CruzRoja

cantidad_datos = int (input('Ingrese los datos que desea ingresar:  '))

for i in range (cantidad_datos):
     nombre = input("Ingrese el nombre del paciente: ")
     apellido = input("Ingrese el apellido del paciente: ")
     año_nacimiento = int(input("Ingrese el año de nacimiento del paciente: "))
     reto5CruzRoja.agregar_nombre(nombre, apellido)
     reto5CruzRoja.agregar_edad(año_nacimiento)


print("\n Lista de PACIENTES:")
reto5CruzRoja.imprimir()


print("\nPaciente mayor y menor:")
reto5CruzRoja.obtener_mayor_menor()


