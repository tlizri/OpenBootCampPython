from src.exercisethree.imc import imc


def main():
    """Main script for exercise three
    :return: None
    :rtype: NoneType
    """
    p = float(input('Indique su peso (kg): '))
    e = float(input('Indique su estatura (m): '))
    print("Tu indice de masa corporal es de " + str(imc(p, e)))


if __name__ == '__main__':
    main()
