# Sovellus painoindeksin ja kehon rasvaprosentin laskemiseen
# -----------

# Kirjastot ja moduulit
import math

# Määritellään funktio painoindeksin laskentaan
def laske_bmi(paino, pituus):
    """Laskee painoindeksin (BMI)

    Args:
        paino (float): paino (kg)
        pituus (float): pituus (cm)

    Returns:
        float: painoindeksi desimaalin tarkkuudella
    """
    pituus = pituus / 100  # muutetaan pituus metreiksi
    bmi = paino / pituus**2
    bmi = round(bmi, 1)
    return bmi


# Määritellään funktio aikuisen kehonrasvaprosentin laskemiseen
def aikuisen_rasvaprosentti(bmi, ika, sukupuoli):
    """_summary_

    Args:
        bmi (float): painoindeksi
        ika (float): henkilön ikä
        sukupuoli (float): 1 -> mies, 0 -> nainen

    Returns:
        float: kehon rasvaprosentti (aikuinen)
    """
    rasvaprosentti = 1.20 * bmi + 0.23 * ika - 10.8 * sukupuoli - 5.4
    rasvaprosentti = round(rasvaprosentti, 1)
    return rasvaprosentti

# Määritellään funktio lapsen kehonrasvaprosentin laskemiseen
def lapsen_rasvaprosentti(bmi, ika, sukupuoli):
    """Laskee lapsen kehon rasvaprosentin

    Args:
        bmi (float): painoindeksi
        ika (float): ikä
        sukupuoli (float): poika -> 1, tyttö -> 0

    Returns:
        float: kehon rasvaprosentti (lapsi)
    """
    rasvaprosentti = 1.51 * bmi - 0.7 * ika - 3.6 * sukupuoli + 1.4
    rasvaprosentti = round(rasvaprosentti, 1)
    return rasvaprosentti

def usa_rasvaprosentti_mies(pituus, vyotaron_ymparys, kaulan_ymparys):
    """Laskee miehen rasvaprosentin USA:n armeijan kaavalla

    Args:
        pituus (float): pituus (cm)
        vyotaron_ymparys (float): vyötärön ympärysmitta (cm)
        kaulan_ymparys (float): kaulan ympärysmitta (cm)

    Returns:
        float: rasvaprosentti
    """
    # Sentit tuumiksi
    pituus = pituus / 2.54
    vyotaron_ymparys = vyotaron_ymparys / 2.54
    kaulan_ymparys = kaulan_ymparys / 2.54

    rasvaprosentti = 86.010 * math.log10(vyotaron_ymparys - kaulan_ymparys) - 70.041 * math.log10(pituus) + 36.76
    rasvaprosentti = round(rasvaprosentti, 1)
    return rasvaprosentti


def usa_rasvaprosentti_nainen(pituus, vyotaron_ymparys, kaulan_ymparys, lantion_ymparys):
    """Laskee naisen rasvaprosentin USA:n armeijan kaavalla

    Args:
        pituus (float): pituus (cm)
        vyotaron_ymparys (float): vyötärön ympärysmitta (cm)
        kaulan_ymparys (float): kaulan ympärysmitta (cm)
        lantion_ymparys (float): lantion ympärysmitta (cm)

    Returns:
        float: rasvaprosentti
    """
    # Sentit tuumiksi
    pituus = pituus / 2.54
    vyotaron_ymparys = vyotaron_ymparys / 2.54
    kaulan_ymparys = kaulan_ymparys / 2.54
    lantion_ymparys = lantion_ymparys / 2.54

    rasvaprosentti = 163.205 * math.log10(vyotaron_ymparys + lantion_ymparys - kaulan_ymparys) - 97.684 * math.log10(pituus) - 78.387
    rasvaprosentti = round(rasvaprosentti, 1)
    return rasvaprosentti

# Suoritetaan seuraavat rivit vain, jos tämä tiedosto on pääohjelma
# Mahdollistaa funktioiden lataamisen toisiin ohjelmiin
# Kun koodi ladataan toiseen tiedostoon,
# if __name__ == "__main__":n alapuolella olevaa koodia ei suoriteta
if __name__ == "__main__":
    # Kysytään käyttäjältä tiedot
    pituus_teksti = input('Kuinka pitkä olet (cm): ')
    try:
        pituus_teksti = pituus_teksti.replace(',', '.')
        pituus = float(pituus_teksti)
    except Exception:
        print("Virheellinen syöte! Syötä vain numeroita/desimaalimerkki.")

    paino_teksti = input('Kuinka paljon painat (kg): ')
    try:
        paino_teksti = paino_teksti.replace(',', '.')
        paino = float(paino_teksti)
    except Exception:
        print("Virheellinen syöte! Syötä vain numeroita/desimaalimerkki.")

    ika_teksti = input('Kuinka vanha olet: ')
    try:
        ika = int(ika_teksti)
    except Exception:
        print("Virheellinen syöte! Syötä vain numeroita.")

    # Accepted inputs
    male_inputs = (
        "1", "mies", "poika", "man", "male", "m"
    )
    female_inputs = (
        "0", "nainen", "tyttö", "woman", "female", "f", "n"
    )

    sukupuoli_teksti = input('Sukupuoli mies, vastaa 1, nainen vastaa 0: ')
    sukupuoli_teksti = sukupuoli_teksti.lower()
    if sukupuoli_teksti in male_inputs:
        sukupuoli = 1
    elif sukupuoli_teksti in female_inputs:
        sukupuoli = 0
    else:
        print("Sukupuolta ei tunnistettu.")


    # Lasketaan painoindeksi funktiolla laske_bmi
    oma_bmi = laske_bmi(paino, pituus)

    # Yli 18 vuotiailla käytetään aikuisen kaavaa
    if ika >= 18:
        oma_rasvaprosentti = aikuisen_rasvaprosentti(oma_bmi, ika, sukupuoli)
    # Muussa tapauksessa käytetään lapsen kaavaa
    else:
        oma_rasvaprosentti = lapsen_rasvaprosentti(oma_bmi, ika, sukupuoli)

    print(f"Painoindeksisi on {oma_bmi} "
        + f"ja kehon rasvaprosentti on {oma_rasvaprosentti}.")

    print("Haluatko laskea myös USA:n puolustusvoimien kehon rasvaprosentin?")
    print("Tähän tarvitaan lisätietoja. (vyötärön-, kaulan- ja naisilla myös lantion-ympärys)")
    lasketaanko_usa = input("Syötä k jos haluat. Muussa tapauksessa enter: ").upper()
    if lasketaanko_usa == "K":
        vyotaron_ymparys_teksti = input("Mikä on vyötärösi ympärys (cm): ")
        try:
            vyotaron_ymparys_teksti = vyotaron_ymparys_teksti.replace(',', '.')
            vyotaron_ymparys = float(vyotaron_ymparys_teksti)
        except Exception:
            print("Virheellinen syöte! Syötä vain numeroita/desimaalimerkki.")

        kaulan_ymparys_teksti = input("Mikä on kaulasi ympärys (cm): ")
        try:
            kaulan_ymparys_teksti = kaulan_ymparys_teksti.replace(',', '.')
            kaulan_ymparys = float(kaulan_ymparys_teksti)
        except Exception:
            print("Virheellinen syöte! Syötä vain numeroita/desimaalimerkki.")

        if sukupuoli == 0:  # Nainen
            lantion_ymparys_teksti = input("Mikä on lantiosi ympärys (cm): ")
            try:
                lantion_ymparys_teksti = lantion_ymparys_teksti.replace(',', '.')
                lantion_ymparys = float(lantion_ymparys_teksti)
            except Exception:
                print("Virheellinen syöte! Syötä vain numeroita/desimaalimerkki.")

            oma_rasvaprosentti_usa = usa_rasvaprosentti_nainen(pituus, vyotaron_ymparys, kaulan_ymparys, lantion_ymparys)
        
        elif sukupuoli == 1:  # Mies
            oma_rasvaprosentti_usa = usa_rasvaprosentti_mies(pituus, vyotaron_ymparys, kaulan_ymparys)
        
        print("USA rasvaprosenttisi on:", oma_rasvaprosentti_usa)
    
    else:
        print("USA rasvaprosenttia ei laskettu. Kiitos!")