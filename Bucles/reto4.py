datos = []  
cantidad = int(input('¿Cuántos datos desea ingresar? '))

for i in range(cantidad):
    numero_datos = input('Ingrese un dato: ')
    try:
        numero_convertido = float(numero_datos)
        datos.append(numero_convertido)  
        print(f'Su lista es {datos}')
    except ValueError:
        datos.append(numero_datos)
        print(f'Su lista es {datos}') 
