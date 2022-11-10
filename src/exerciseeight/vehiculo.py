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

    def getProperties(self) -> tuple[str, int, int]:
        """
        :return: return class attributes
        :rtype: tuple[str, int, int]
        """
        return self.color, self.ruedas, self.puertas
