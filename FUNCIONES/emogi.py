def encontrarPalabra (frase):
    if 'feliz' in frase:
        print ('El emogi que te representa es :\U0001F600 ')
    elif 'trsite' in frase: 
        print ('El emogi que te representa es :\U0001F972 ')

lista = []

def agregar_frase(frase):
    lista.append(frase)
    print(f'La frase fue agregada correctamente: {lista}')