from src.exercisefive.bisiesto import isbisiesto


def main():
    """Main script for exercise five
    :return: None
    :rtype: NoneType
    """
    year = input('Introduzca un año: ')
    if isbisiesto(int(year)):
        print('El año ' + year + ' es bisiesto')
    else:
        print('El año ' + year + ' no es bisiesto')


if __name__ == '__main__':
    main()
