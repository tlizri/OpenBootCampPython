# IMPORT
from time import localtime, time, sleep

# CONSTANT
ENDWORK = (19, 0, 0)  # End work time
WORKTIME = 8  # Work hours


# FUNCTION
def diffTime(actual: list, end: tuple) -> int:
    """Calculate substraction between two times in seconds
    :param end: end time in format Hours, Minutes, Seconds
    :type end: tuple
    :param actual: start time in format Hours, Minutes, Seconds
    :type actual: tuple
    :return: substraction of end time and start time in hours
    :rtype: int
    """
    diff = 0
    diff += end[2] - actual[2]
    diff += (end[1] - actual[1]) * 60
    diff += (end[0] - actual[0]) * (60 * 60)
    return diff


def toTimeFormat(sec: int) -> list:
    """Transform seconds in format Hours, Minutes, Seconds
    :param sec: seconds to transform
    :type sec: int
    :return: secos transformed in format Hours, Minutes, Seconds
    :rtype: list
    """
    horas = sec // (60 * 60)
    minutos = (sec // 60) - (horas * 60)
    segundos = sec - (horas * 60 * 60) - (minutos * 60)
    return [horas, minutos, segundos]


def showTime(t: list):
    """Show in terminal the time in format 'Faltan HH hora(s) mm minuto(s) ss segundo(s)
    every second
    :param t: time to show in format (HH, mm, ss)
    :type t: list
    :return: None
    :rtype: NoneType
    """
    msg = 'Faltan '
    msg += '0' + str(t[0]) if t[0] < 10 else str(t[0])
    msg += ' hora ' if t[0] == 1 else ' horas '
    msg += '0' + str(t[1]) if t[1] < 10 else str(t[1])
    msg += ' minuto ' if t[1] == 1 else ' minutos '
    msg += '0' + str(t[2]) if t[2] < 10 else str(t[2])
    msg += ' segundo ' if t[2] == 1 else ' segundos '
    print(msg, end='\r')
    sleep(1)


def isHomeTime():
    """Function calculate the time left until work end show it every second
    :return: None
    :rtype: NoneType
    """
    actual = list(localtime(time())[3:6])  # Current time in (HH, mm, ss)
    diff = diffTime(actual, ENDWORK)
    left = toTimeFormat(diff)
    if 0 == left[0] and (left[1] > 0 or left[2] > 0):
        showTime(left)
        return False
    elif ENDWORK[0] - WORKTIME == left[0] and left[1] == 0 and left[2] == 0:
        showTime(left)
        return False
    elif 0 < left[0] < ENDWORK[0] - WORKTIME:
        showTime(left)
        return False
    else:
        print('Hora de ir a casa', end='\r')
        return True
