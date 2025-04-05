from lapto import Laptop
from  laptopGaming import Laptop_Gaming

laptop_pepito = Laptop('Lenovo','i7',32)
laptop_maria = Laptop('Lenovo','i7',32,600)


lapto_juanito = Laptop_Gaming('MSI','i7',4,'RTX 8G')


def imprimirInforme (lapto):
    informe = lapto.realizar_informe_uso()
    for clave,valor in informe.items():
        print(f'{clave} ; {valor}')
    print('\n ')
    
print ('JUANITO :')
imprimirInforme(lapto_juanito)
print('PEPITO')
imprimirInforme(laptop_pepito)

