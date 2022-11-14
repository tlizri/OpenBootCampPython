def noContieneNumeros(lista: list[str]) -> bool:
    """Check if a list has alphabetic characters, white space included
    :param lista: list of strings
    :type lista:
    :return: true if all elements are alphabetic characters
    :rtype: bool
    """
    return all(x.replace(' ', '').isalpha() for x in lista)


def transformarLista(paises: list[str]) -> list[str]:
    """Function that sort the list of strings,
    remove repeated elements and capitalize the first character of the string
    :param paises: string list to be treated
    :type paises: list[str]
    :return: transformed string list
    :rtype: list[str]
    """
    paises = sorted(list(x.lower() for x in paises))
    paises = list(set(paises))
    paises = list(x.title() for x in paises)
    return paises


def inputPaises() -> list[str]:
    """Function that take user input separated by coma and return a list of strings
    :return: the user input in a list of strings
    :rtype: list[str]
    """
    paises = input('Escribe una lista de paises separados por coma: ').split(sep=',')
    return list(x.strip() for x in paises)


def getPaises() -> tuple[int, list[str]]:
    """Function that take a list of countries from user,
    check if it has alphabetic characters,
    apply a data transform, then return if it has errors and the list of strings.
    :return: a tuple where the first element is 0 if there is error in the process
             or 1 if correct. The second element is the list of strings.
    :rtype: tuple[int, list[str]]
    """
    paises = list()
    temp = inputPaises()
    if noContieneNumeros(temp):
        paises.extend(temp)
        transformarLista(paises)
        return 0, paises
    else:
        return 1, temp
