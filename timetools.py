# Tools for date and time calculations

# Libraries and modules
import datetime  # Python's internal datetime module


# Aika ero kahden päivämäärän välillä
def datediff(d1, d2):
    """Calculates the difference between two dates in days

    Args:
        d1 (str): A date in ISO format (YYYY-MM-DD)
        d2 (str): A date in ISO format (YYYY-MM-DD)

    Returns:
        int: Absolute difference in days
    """
    d1 = datetime.datetime.strptime(d1, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(d2, '%Y-%m-%d')
    difference = abs((d2 - d1).days)
    return difference

# datediff testi:
# ero = datediff('2023-03-17', '2023-01-20')
# print(f"Ero päivinä: {ero}pv")


# Funktio, joka laskee kahden kellonajan välisen eron tunteina
def timediff(t1, t2):
    """Calculates the difference between two times in hours

    Args:
        t1 (str): Time in format hh:mm:ss
        t2 (str): Time in format hh:mm:ss

    Returns:
        float: Time difference in hours
    """
    t1 = datetime.datetime.strptime(t1, '%H:%M:%S')
    t2 = datetime.datetime.strptime(t2, '%H:%M:%S')

    # Calculates a timedelta which supports only seconds and microseconds
    seconds = abs((t2 - t1).seconds)
    # Minute = 60seconds, Hour = 60minutes, 60*60 = 3600
    hours = seconds / 3600
    return hours

# timediff testi:
# kesto = timediff('10:00:00', '14:30:00')
# print(f"Kesto: {kesto}h")


def datediff2(d1, d2, unit):
    """Calculates the difference between two dates in selected unit

    Args:
        d1 (str): A date in ISO format (YYYY-MM-DD)
        d2 (str): A date in ISO format (YYYY-MM-DD)
        unit (str): Unit to return (day/year)

    Returns:
        float: Difference in selected unit
    """
    # TODO: vertaa mikan filuun, onko esim kuukaudet
    d1 = datetime.datetime.strptime(d1, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(d2, '%Y-%m-%d')
    difference = abs((d2 - d1).days)  # Timedelta in days

    if unit.lower() == 'day':
        return difference
    elif unit.lower() == 'year':
        return difference / 365

    # Same with dictionary
    # units = { # Dict for unit dividers
    #     'day': 1,
    #     'year': 365
    # }
    # divider = units[unit.lower()] # Choose divider by unit arg
    # return difference / divider # Return in years or days

def timediff2(t1, t2, unit):
    """Calculates the difference between two times in chosen unit

    Args:
        t1 (str): Time in format hh:mm:ss
        t2 (str): Time in format hh:mm:ss
        unit (str): Unit to return

    Returns:
        float: Time difference in hours
    """
    t1 = datetime.datetime.strptime(t1, '%H:%M:%S')
    t2 = datetime.datetime.strptime(t2, '%H:%M:%S')
    units = {
        'hour': 3600,
        'minute': 60,
        'second': 1
    }
    seconds = abs((t2 - t1).seconds)
    divider = units[unit.lower()]  # Choose divider by unit arg
    value = seconds / divider
    return value

if __name__ == '__main__':
    # Test date difference
    date1 = '2023-03-21'
    date2 = '2023-03-17'
    ero = datediff2(date1, date2, 'day')
    print(f"Ero oli: {ero}pv.")

    # Test time difference
    time1 = '10:00:00'
    time2 = '15:25:00'
    ero = timediff2(time1, time2, 'hour')
    print(f"Ero oli: {ero:.2f}h.")

    ero = timediff2(time1, time2 , 'minute')
    print (f"Ero minuuteissa: {ero}min.")