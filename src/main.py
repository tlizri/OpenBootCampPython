from src.exercisesix.alumno import Alumno


def main():
    """Main script for exercise six.b
    :return: None
    :rtype: NoneType
    """
    alumno = Alumno()
    alumno.asignarNombre('Rafael')
    alumno.asignarNota(10)
    alumno.verDatos()
    alumno.estaAprovado()


if __name__ == '__main__':
    main()
