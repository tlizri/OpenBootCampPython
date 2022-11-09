def _mostrar(a, b, c, operacion):
    """Function to show the operation and its result
    :param a: first operand
    :type a: numerical
    :param b: second operand
    :type b: numerical
    :param c: result of the operation
    :type c: numerical
    :param operacion: type of the operation
    :type operacion: str
    :return: None
    :rtype: NoneType
    """
    print(a, operacion, b, '=', c)


def sumar(a, b):
    """Function to calculate addition of two numbers
    :param a: first operand
    :type a: numerical
    :param b: second operand
    :type b: numerical
    :return: addition of two operands
    :rtype: numerical
    """
    c = a + b
    _mostrar(a, b, c, '+')
    return c


def restar(a, b):
    """Function to calculate subtraction of two numbers
    :param a: first operand
    :type a: numerical
    :param b: second operand
    :type b: numerical
    :return: subtraction of two operands
    :rtype: numerical
    """
    c = a - b
    _mostrar(a, b, c, '-')
    return c


def multiplicar(a, b):
    """Function to calculate multiplication of two numbers
    :param a: first operand
    :type a: numerical
    :param b: second operand
    :type b: numerical
    :return: multiplication of two operands
    :rtype: numerical
    """
    c = a * b
    _mostrar(a, b, c, '*')
    return c


def dividir(a, b):
    """Function to calculate division of two numbers
    :param a: first operand
    :type a: numerical
    :param b: second operand
    :type b: numerical
    :return: division of two operands, infinite if divide by zero
    :rtype: numerical
    """
    if b != 0:
        c = a / b
        _mostrar(a, b, c, '/')
        return c
    else:
        c = float('inf')
        _mostrar(a, b, c, '/')
        return float('inf')
