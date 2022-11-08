from src.exercisesix.vehiculo import Coche


def main():
    """Main script for exercise six-a
    :return: None
    :rtype: NoneType
    """
    micoche = Coche(cilindrada=1299, velocidad=180, color='rojo', ruedas=4, puertas=5)
    print('Cilindradas:', micoche.cilindrada, 'cc')
    print('Velocidad:', micoche.velocidad, 'km/h')
    print('Color:', micoche.color)
    print('Ruedas:', micoche.ruedas)
    print('Puertas:', micoche.puertas)


if __name__ == '__main__':
    main()
