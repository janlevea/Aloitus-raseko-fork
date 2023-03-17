# Esimerkkejä päivämäärien, tiedostojen ja JSON-tietojen käytöstä
import datetime # Pythonin sisäinen kirjasto aikamuotojen käsittelyyn
import json # Pythonin sisäinen kirjasto JSON-tietojen käsittelyyn

# Päiväyksen muodostaminen
year = 2023
month = 3
day = 17

date = datetime.datetime(year, month, day)

print(date)

# Kuluvan päivän ja kellonajan selvittäminen
just_now = datetime.datetime.now()
print(just_now)

# Aika ero kahden päivämäärän välillä
def datediff(d1, d2):
    """Calculates the difference between two dates in days

    Args:
        d1 (str): A date(before) in ISO format (YYYY-MM-DD)
        d2 (str): A date(after) in ISO format (YYYY-MM-DD)

    Returns:
        int: Absolute difference in days
    """
    d1 = datetime.datetime.strptime(d1, '%Y-%m-%d')
    d2 = datetime.datetime.strptime(d2, '%Y-%m-%d')
    difference = abs((d2 - d1).days)
    return difference

ero = datediff('2023-03-17', '2023-01-20')
print(f"Ero päivinä: {ero}pv")

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
    seconds = abs((t2 - t1).seconds)
    hours = seconds / 3600
    return hours

kesto = timediff('10:00:00', '14:30:00')
print(f"Kesto: {kesto}h")

# Määritellään Python sanakirja
jumppari = {
    'nimi': 'Erkki',
    'pituus': 171,
    'paino': 75.5, 
}

# Luodaan JSON-merkkijono sanakirjasta
json_jumppari = json.dumps(jumppari)
print(json_jumppari)