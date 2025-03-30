from auto import auto

autO1= auto('FORD','EXPLORER','2025',1001)
autO2= auto('FORD','RANGER','2025',100)
autO3= auto('FORD','RANGER','2025',100)


auto.compararKilometraje(autO1,autO2)
auto.compararMarca(autO1,autO2)

for numero in range (1,3):
    carroNuevo = auto.crearAuto()
    print(carroNuevo.__dict__)

auto.agregarUnaMarca(autO1,autO2,autO3)
