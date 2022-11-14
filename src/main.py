from exercisenine.countries import getPaises


def mostrarPaises(paises: list[str]):
    """Show in terminal the list of countries separated by comma.
    :param paises: lista de paises
    :type paises: list[str]
    """
    msg = ''
    msg += paises[0]
    for pais in paises[1:len(paises)]:
        msg += ', '
        msg += pais
    print(msg)


def main():
    """Main script for exercise nine A
    """
    error, paises = getPaises()
    if error == 0:
        mostrarPaises(paises)
    else:
        print(f'Error al introducir paises: {paises}')


# Reino Unido, Italia, España, Francia
if __name__ == '__main__':
    main()
