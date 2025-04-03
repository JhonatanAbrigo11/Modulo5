from lapto import Laptop
from  laptopGaming import Laptop_Gaming

laptop_pepito = Laptop('Lenovo','i7','32 G')
laptop_maria = Laptop('Lenovo','i7','32 G',600)


lapto_juanito = Laptop_Gaming('MSI','i7',4,'RTX 8G')
print(lapto_juanito.realizar_diagnostico_sistema())

