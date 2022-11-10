# LIBRARIES
from sys import argv

from exerciseeight.filemanage import FileManager

# CONSTANT
PATH = 'src/files/path.txt'


# FUNCTIONS
def argsTransformation(args: list[str], argc: int) -> str:
    """Function to process main arguments in a sigle string
    :param args: string list to be processed
    :type args: list[str]
    :param argc: size of args
    :type argc: int
    :return: string list in a unique string
    :rtype: str
    """
    text = ''
    for arg in args[1:argc]:
        if arg == args[argc - 1]:
            text += arg
        else:
            text += arg + ' '
    text += '\n'
    return text


def readPaths() -> tuple[str, str]:
    """Function to read a file with path.txt data
    :return: return path.txt and filename
    :rtype: tuple[str, str]
    """
    f = open(PATH, 'r')
    paths = f.readlines()
    f.close()
    split = []
    for path in paths:
        split.append(path.split('='))
    path = ''
    filename = ''
    for linea in split:
        if linea[0] == 'PATH':
            path = linea[1].replace('\n', '')
        if linea[0] == 'FILENAME':
            filename = linea[1].replace('\n', '')
    return path, filename


# MAIN FUNCTION
def main(args, argc):
    """Main script for exercise eight A
    :return: None
    :rtype: NoneType
    """
    # Convert arguments in one string
    text = argsTransformation(args, argc)
    # Take path.txt and filename from files/path.txt
    path, filename = readPaths()
    # Create file manager object
    f = FileManager(path, filename)
    # Create text file
    f.createTextFile()
    # Write arguments in text file
    f.writeTextFile(text)


if __name__ == '__main__':
    main(argv, len(argv))
