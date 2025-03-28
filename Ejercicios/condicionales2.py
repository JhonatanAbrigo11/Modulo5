import random

aleatorio = random.randint(1,9)
aleatorio_dos = random.randint(1,9)

if aleatorio == 4: 
    print ('TE GANASTE UN CHUPETE!!!')
elif aleatorio == 8:
    print ('TE GANASTE UN BALÓN')
elif aleatorio == 3 and aleatorio_dos == 7: 
    print('TE GANASTE UN TELEVISOR')
else: 
    print ('PERDISTE !!')