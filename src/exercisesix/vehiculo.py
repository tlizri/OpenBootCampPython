class Vehiculo:
    """Conceptual representation of a vehicle
    :param color: representation of vehicle color
    :type color: str
    :param ruedas: number of wheels
    :type ruedas: int
    :param puertas: number of doors
    :type puertas: int
    """
    def __init__(self, color='', ruedas=-1, puertas=-1):
        """Constructor method
        """
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class Coche(Vehiculo):
    """Conceptual representation of a car that inherits from vehicle
    :param velocidad: car speed
    :type velocidad: int
    :param cilindrada: car cylinder
    :type cilindrada: int
    :param color: representation of vehicle color
    :type color: str
    :param ruedas: number of wheels
    :type ruedas: int
    :param puertas: number of doors
    :type puertas: int
    """
    def __init__(self, velocidad=-1, cilindrada=-1, color='', ruedas=-1, puertas=-1):
        """Constructor method
        """
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
