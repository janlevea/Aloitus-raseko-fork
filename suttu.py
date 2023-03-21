# Esimerkkejä päivämäärien, tiedostojen ja JSON-tietojen käytöstä
import datetime # Pythonin sisäinen kirjasto aikamuotojen käsittelyyn
import json # Pythonin sisäinen kirjasto JSON-tietojen käsittelyyn

# # Päiväyksen muodostaminen
# year = 2023
# month = 3
# day = 17

# date = datetime.datetime(year, month, day)

# print(date)

# # Kuluvan päivän ja kellonajan selvittäminen
# just_now = datetime.datetime.now()
# print(just_now)

# JSON JUTTUJA

# Luodaan tyhjä lista pinon perustaksi
jumppari_lista = []

# Määritellään Python sanakirja
jumppari = {
    'nimi': 'Erkki',
    'pituus': 171,
    'paino': 75.5, 
}
jumppari2 = {
    'nimi': 'Essi',
    'pituus': 165,
    'paino': 60.5,
}

# Lisätään jumpparit listaan
jumppari_lista.append(jumppari)
jumppari_lista.append(jumppari2)
print(jumppari_lista)

"""
# Luodaan JSON-merkkijono sanakirjasta
json_jumppari = json.dumps(jumppari)
print(json_jumppari)

# Luodaan tiedosto
try:
    file_to_use = open("kuntoilijat.json", "x")
    file_to_use.close() # Suljetaan tiedosto
except:
    print("Tiedosto on jo olemassa")
finally:
    file_to_use.close()

# Kirjoitetaan tiedostoon JSON-objekti
file_to_use = open("kuntoilijat.json", "w")
# Muutetaan sanakirja JSON-muotoon ja tallennetaan tiedostoon
json.dump(jumppari, file_to_use, indent=4)
file_to_use.close()


# Luetaan tiedostosta JSON-objekti
file_to_use = open("kuntoilijat.json", "r")
data = json.load(file_to_use)
file_to_use.close()
print("Luettu data:", data)

# Lisätään toinen JSON-objekti tiedoston loppuun
# file_to_use = open("kuntoilijat.json", "a")
# file_to_use.close()

# with-syntaksi sulkee tiedoston automaattisesti ja on järkevämpi tapa kirjoittaa/lukea tiedosto.
with open('kuntoilijat.json', 'a') as file_to_use:
    json.dump(jumppari2, file_to_use, indent=4)
"""
# Avataan tiedosto kirjoitustilaan ja tallennetaan lista
with open('kuntoilijat.json', 'w') as file:
    json.dump(jumppari_lista, file, indent=4)

# Avataan tiedosto lukutilaan
with open('kuntoilijat.json', 'r') as file:
    read_data = json.load(file) # Luetaan lista
    last_data = read_data[-1] # Haetaan viimeinen alkio listasta
    print(last_data) # Tulostetaan viimeinen alkio

"""
poptesti = ["moi", "hei", "terve"]

print(poptesti.pop())
print(poptesti.pop())

print(poptesti)
"""