class Alumno:
    """Conceptual representation of a student
    """
    def __init__(self, nombre='', nota=-1):
        """Constructor method
        :param nombre: student name
        :type nombre: str
        :param nota: student mark
        :type nota: float
        """
        self.nombre = nombre
        self.nota = float(nota)

    def asignarNombre(self, nombre=''):
        """Method to assign a student name
        :param nombre: student name
        :type nombre: str
        :return: None
        :rtype: NoneType
        """
        self.nombre = nombre

    def asignarNota(self, nota=-1):
        """Method to assign a student mark
        :param nota: student mark
        :type nota: float
        :return: None
        :rtype: NoneType
        """
        self.nota = float(nota)

    def verDatos(self):
        """Method to show student data
        :return: None
        :rtype: NoneType
        """
        print('Alumno:', self.nombre)
        print('Calificacion:', self.nota)

    def estaAprovado(self):
        """Method to check if the student pass or fail
        :return: None
        :rtype: NoneType
        """
        if self.nota >= 5:
            print('Aprobado')
        else:
            print('Suspenso')
