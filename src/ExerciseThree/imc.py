def imc():
    p = float(input('Indique su peso (kg): '))
    e = float(input('Indique su estatura (m): '))
    icm = round(p/(e*e), 2)
    print('Tu Indice de Masa Corporal es: ' + str(icm))
