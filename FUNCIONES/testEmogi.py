import emogi 

cantidadFrase= int(input('Cuantas frases desea ingresar:  '))
for i in range(cantidadFrase):
    frase = input('Ingrese la frase:  ')
    emogi.encontrarPalabra(frase)
    emogi.agregar_frase(frase)
     
    
