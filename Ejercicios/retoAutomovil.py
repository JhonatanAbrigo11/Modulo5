print ('****** ¡Viaja con KrakeTravels!*****')
destino = input('Ingrese cual es su destino del viaje: COLOMBIA, ECUADOR, PERU:   ')
zona = input ('Ingrese por la zona donde está: ZONA URBANA, ZONA RURAL O PERIMETRAL:  ')
tiempo = int (input('Ingrese la velocidad con la que esta yendo km/h:    '))

if destino == 'ECUADOR':
    if zona == 'ZONA URBANA'  and tiempo >= 50 :
        print('SU VELOCIDAD ES MÁXIMA')
    elif zona == 'ZONA RURAL' and tiempo >=70: 
        print('SU VELOCIDAD ES MÁXIMA')
    elif zona == 'ZONA PERIMETRAL' and tiempo  >=90:
        print('SU VELOCIDAD ES MÁXIMA')
    else: 
        print ('SU VELOCIDA ES MÍNIMA')
elif destino == 'COLOMBIA':
    if zona == 'ZONA URBANA'   and tiempo >= 30 :
        print('SU VELOCIDAD ES MÁXIMA')
    elif zona == 'ZONA RURAL' and tiempo >=80: 
        print('SU VELOCIDAD ES MÁXIMA')
    elif zona == 'ZONA PERIMETRAL' and tiempo  >=100:
        print('SU VELOCIDAD ES MÁXIMA')
    else: 
        print ('SU VELOCIDA ES MÍNIMA')
elif destino == 'PERU':
    if zona == 'ZONA URBANA'   and tiempo >= 40 :
        print('SU VELOCIDAD ES MÁXIMA')
    elif zona == 'ZONA RURAL' and tiempo >=60: 
        print('SU VELOCIDAD ES MÁXIMA')
    elif zona == 'ZONA PERIMETRAL' and tiempo  >=120:
        print('SU VELOCIDAD ES MÁXIMA')
    else: 
        print ('SU VELOCIDA ES MÍNIMA')
else: 
    print ('EL DESTINO NO ESTA EN LA LISTA')

