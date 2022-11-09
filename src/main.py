from time import sleep


from exerciseseven.ishometime import isHomeTime


def main():
    """Main script for exercise seven B
    :return: None
    :rtype: NoneType
    """
    home = False
    while not home:
        home = isHomeTime()


if __name__ == '__main__':
    main()
