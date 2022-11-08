def imc(p=0, e=0):
    """Script that calculate the body mass index rounded to two decimal places
    :param p: user weigth
    :type p: float
    :param e: user height float
    :type e: float
    :return: body mass index rounded to two decimal places
    :rtype: float
    """
    return round(p/(e*e), 2)
