from lapto import Laptop


laptop_pepito = Laptop('Lenovo','i7','32 G')
laptop_maria = Laptop('Lenovo','i7','32 G',600)


for numero in range (1,3):
    asus_Laptop = Laptop.asus_laptop(numero)
    print (asus_Laptop.__dict__)

print (laptop_pepito.__dict__)
print (laptop_pepito.valor_final())
print (f"El valor descuento : {laptop_pepito.valor_descuento(10)}")

print(Laptop.comparar_costo(laptop_pepito,laptop_maria))