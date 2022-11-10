# LIBRARIES
from src.exerciseeight.saveobject import ObjectManager
from src.exerciseeight.vehiculo import Vehiculo

# CONSTANT
PATH = 'src/files/path.txt'


# FUNCTION
def readPaths() -> tuple[str, str, str]:
    """Function to read a file with path.txt data
    :return: return path.txt, file name, binary file name
    :rtype: tuple[str, str, str]
    """
    f = open(PATH, 'r')
    paths = f.readlines()
    f.close()
    split = []
    for path in paths:
        split.append(path.split('='))
    bfilename = ''
    path = ''
    filename = ''
    for linea in split:
        if linea[0] == 'PATH':
            path = linea[1].replace('\n', '')
        if linea[0] == 'FILENAME':
            filename = linea[1].replace('\n', '')
        if linea[0] == 'BFILENAME':
            bfilename = linea[1].replace('\n', '')
    return path, filename, bfilename


# MAIN FUNCTION
def main():
    """Main script for exercise eight B
    :return: None
    :rtype: NoneType
    """
    coche = Vehiculo(color='carbon', ruedas=4, puertas=5)
    print(coche.getProperties())
    path, _, bfile = readPaths()
    obj = ObjectManager(path, bfile, coche)
    print('Aparcar coche')
    obj.saveObject()
    print('Olvidar coche')
    del coche, obj
    obj = ObjectManager(path, bfile)
    print('Recordar coche')
    coche = obj.loadObject()
    if coche is None:
        pass
    else:
        print(coche.getProperties())


if __name__ == '__main__':
    main()
