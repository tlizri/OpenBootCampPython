def isbisiesto(year):
    """Script to check if an input year is leap year
    :param year: year to check if is leap year
    :type year: int
    :return: True if is leap year, False if is not
    :rtype: bool
    """
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
