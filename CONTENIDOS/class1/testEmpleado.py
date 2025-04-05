
from empeladoTC import empleadoTiempoCompleto
from EmpleadoMT import empleadoMedioTiempo

empleado1= empleadoMedioTiempo('Jhonatan',400)
empleado2= empleadoTiempoCompleto('Alexis',600)
print('EMPLEADO 1:',empleado1.calcular_salario())
print('EMPLEADO 2:',empleado2.calcular_salario())

empleados = [
    empleadoMedioTiempo('Jhonatan',400),
    empleadoMedioTiempo('Juan',400),
    empleadoTiempoCompleto('Alexis',600),
    empleadoMedioTiempo('Jinson',400),
    empleadoTiempoCompleto('Pablo',600)  
]

for empleado in empleados:
    print(empleado.calcular_salario())
    