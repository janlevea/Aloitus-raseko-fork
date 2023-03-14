# Ohjelma joka kysyy bmi-tietoja useasta kuntoilijasta
# ---------------

# Kirjastot ja modulit
# Tuodaan fitness.py:n sisältämät toiminnot tähän ohjelmaan
import fitness

# Kysytään tiedot ja tulostetaan painoindeksi kunnes halutaan lopettaa
bmi_lista = []
nimilista = []

while True:  # Ikuinen silmukka, jossa ollaan kunnes annetaan tyhjä nimi
    
    nimi = input('Nimi, tyhjä lopettaa: ')
    
    if nimi == '':
        break 

    nimilista.append(nimi)
    pituus_teksti = input('Pituus (cm) ')
    try:
        pituus_teksti = pituus_teksti.replace(',', '.')  # Muuta , pisteksi
        pituus = float(pituus_teksti)
    except Exception:
        print("Virheellinen syöte! Syötä vain numeroita/desimaalimerkki.")

    paino_teksti = input('Paino (kg): ')
    try:
        paino_teksti = paino_teksti.replace(',', '.')  # Muuta , pisteksi
        paino = float(paino_teksti)
    except Exception:
        print("Virheellinen syöte! Syötä vain numeroita/desimaalimerkki.")

    # Yritetään laskea bmi ja lisätä tiedot listaan monikkona
    try:
        # Lasketaan painoindeksi fitness-moduulin laske_bmi-funktiolla
        bmi = fitness.laske_bmi(paino, pituus)
        # Luodaan monikko (tuple), jossa nimi ja bmi
        monikko = (nimi, bmi)
        # Lisätään monikko listaan
        bmi_lista.append(monikko)
        # Näytetään painoindeksi ruudulla
        print('Painoindeksi on', bmi)
    except Exception as e:
        print("Virhe BMI:n laskemisessa ja tietojen listaan lisäämisessä.")
        print(e)

# Tulosta ruudulle lopuksi lista painoindekseistä
print('Nimet ja painoindeksit olivat:')
print(bmi_lista)
print() # Tyhjä rivi

# Puretaan lista ja tulostetaan se rivi-riviltä -> monikko / rivi
for henkilo in bmi_lista:
    # Monikossa on kaksi tietoa, joiden indeksit ovat 0 (ensimmäinen) ja 1 (toinen)
    print(henkilo[0], 'painoindeksi on', henkilo[1] + ".")
    
# Listassa olevien monikoiden määrä
print('Listassa oli', len(bmi_lista), 'merkintää.')

# Harjoitus: Tee bmi-listan perusteella kuntoilijoiden aakkostettu nimilista
nimilista.sort() # Aakkostetaan nimilista
print(nimilista) # Tulostetaan se