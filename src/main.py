from sys import argv

from exercisenine.sumarimpares import sumarImpares


def showCalculation(lista: list[int], resultado: int):
    """Function that show in terminal the operation
    :param lista: list of digit to operate
    :type lista: list[int]
    :param resultado: result of the operation
    :type resultado: int
    """
    msg = str(lista[0])
    for digito in lista[1:len(lista)]:
        msg += ' + '
        msg += str(digito)
    print(f'{msg} = {resultado}')


def main(args, argc):
    """Main script for exercise nine B.
    """
    if argc < 1:
        print('Introduzca algún digito entero')
        exit(1)
    error, resultado, impares = sumarImpares(args)
    if error == 0:
        showCalculation(impares, resultado)
        exit(error)
    elif error == 1:
        print('No hay elementos que sumar')
        exit(error)
    elif error == 2:
        print('Error, hay elementos no numéricos')
        exit(error)


if __name__ == '__main__':
    main(argv[1:len(argv)], len(argv[1:len(argv)]))
