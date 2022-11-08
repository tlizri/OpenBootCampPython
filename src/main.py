import ExerciseFive.isBisiesto as e5


def main():
    year = input('Introduzca un año: ')
    if e5.isBisiesto(int(year)):
        print('El año ' + year + ' es bisiesto')
    else:
        print('El año ' + year + ' no es bisiesto')


if __name__ == '__main__':
    main()
