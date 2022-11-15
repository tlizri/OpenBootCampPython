from functools import reduce


def isNumeric(lista: list[str]) -> bool:
    """Check if a list of strings are numeric
    :param lista: list of strings to check
    :type lista: list[str]
    :return: true if all elements in the list are numeric, false otherwise
    :rtype: bool
    """
    return all(x.isnumeric() for x in lista)


def strToInt(lista: list[str]) -> list[int]:
    """Transform a list of strings to a list of integers
    :param lista: list of strings to transform
    :type lista: list[str]
    :return: list of strings transformed in integer
    :rtype: list[int]
    """
    return list(int(x) for x in lista)


def isImpar(a: int) -> bool:
    """Check if a number is odd.
    :param a: number to check
    :type a: int
    :return: true if the numbers is odd, false otherwise
    :rtype: bool
    """
    if a % 2 != 0:
        return True
    return False


def getImpares(lista: list[int]) -> list[int]:
    """Function that filter a list of integers and take odd numbers
    :param lista: list of integers to filter
    :type lista: list[int]
    :return: list filtered with odd numbers
    :rtype: list[int]
    """
    return list(filter(isImpar, lista))


def sumar(a: int, b: int) -> int:
    """Function to add two numbers
    :param a: first operand
    :type a: int
    :param b: second operand
    :type b: int
    :return: addition of the operands
    :rtype: int
    """
    return a + b


def sumarImpares(lista: list[str]) -> tuple[int, int, list[int]]:
    """Function that check if a list of strings are numerics,
    then check if the list is not empty, take the odd numbers of the list,
    finally make arithmetic addition with all odd numbers of the list
    :param lista: list of integers
    :type lista: list[str]
    :return: error -> 0 if correct, 1 if the list is empty, 2 if the list is not numeric
             result of the operation
             list of the operands
    :rtype: tuple[int, int, list[int]]
    """
    if isNumeric(lista):
        lista = getImpares(strToInt(lista))
        if len(lista) != 0:
            return 0, reduce(sumar, lista), lista
        else:
            return 1, 1, []
    return 2, 1, []
