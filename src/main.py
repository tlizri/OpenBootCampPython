import sys
from src.exercisetwo.helloworld import helloworld


def main(argv):
    """Main script for exercise two
    :param argv: list of arguments for helloworld script
    :type argv: list(str)
    :return: None
    :rtype: NoneType
    """
    if len(argv) == 0:
        helloworld()
    else:
        helloworld(argv[0])


if __name__ == '__main__':
    main(sys.argv[1:])
