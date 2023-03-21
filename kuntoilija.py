# Kuntoilijan tiedot oliona
# -----------

# Kirjastot ja modulit (libraries and modules)
import fitness

# Luokkamääritykset (class definitions)
# Kuntoilija-luokka - Yliluokka JunioriKuntoilijalle (super class)
class Kuntoilija:
    """Luokka kuntoilijan tietoja varten"""

    # Olionmuodostin eli konstruktori, self -> tuleva olio
    # Jos vyötärön, kaulan tai lantion ympärysmittoja ei anneta, niin ne asetetaan oletusarvoiksi 0.0
    def __init__(self, nimi, pituus, paino, ika, sukupuoli, paiva, vyotaron_ymparys=0.0, kaulan_ymparys=0.0, lantion_ymparys=0.0):

        # Määritellään tulevan olion ominaisuudet (property) eli luokan kentät (field)
        self.nimi = nimi
        self.pituus = pituus
        self.paino = paino
        self.ika = ika
        self.sukupuoli = sukupuoli
        self.bmi = fitness.laske_bmi(self.paino, self.pituus)
        self.punnitus_paiva = paiva

        self.vyotaron_ymparys = vyotaron_ymparys
        self.kaulan_ymparys = kaulan_ymparys
        self.lantion_ymparys = lantion_ymparys

        self.usa_rasvaprosentti = 0.0

    # Metodi rasvaprosentin laskemiseen (yleinen / aikuinen)
    def rasvaprosentti(self):
        self.rasvaprosentti = fitness.aikuisen_rasvaprosentti(
            self.bmi, self.ika, self.sukupuoli)
        return self.rasvaprosentti

    def laske_usa_rasvaprosentti(self):
        if self.sukupuoli == 1:  # Mies
            if self.vyotaron_ymparys == 0.0 or self.kaulan_ymparys == 0.0:
                print("USA:n armeijan rasvaprosenttikaava vaatii vyötärön ja kaulan ympärysmitat.")
                self.usa_rasvaprosentti = 0.0
            else:
                self.usa_rasvaprosentti = fitness.usa_rasvaprosentti_mies(
                    self.pituus, self.vyotaron_ymparys, self.kaulan_ymparys
                )
        elif self.sukupuoli == 0:  # Nainen
            if self.vyotaron_ymparys == 0.0 or self.kaulan_ymparys == 0.0 or self.lantion_ymparys == 0.0:
                print("USA:n armeijan rasvaprosenttikaava vaatii vyötärön, kaulan ja lantion ympärysmitat.")
                self.usa_rasvaprosentti = 0.0
            else:
                self.usa_rasvaprosentti = fitness.usa_rasvaprosentti_nainen(
                    self.pituus, self.vyotaron_ymparys, self.kaulan_ymparys, self.lantion_ymparys
                )
        return self.usa_rasvaprosentti

# JunioriKuntoilija-luokka Kuntoilija-luokan aliluokka (subclass)
class JunioriKuntoilija(Kuntoilija):
    """Luokka nuoren kuntoilijan tiedoille"""

    # Konstruktori
    def __init__(self, nimi, pituus, paino, ika, sukupuoli):

        # Määritellään periytyminen, mitä ominaisuuksia perii yliluokasta (Kuntoilija)
        super().__init__(nimi, pituus, paino, ika, sukupuoli)
        self.bmi = fitness.laske_bmi(self.paino, self.pituus)

    # Metodi rasvaprosentin laskemiseen (ylikirjoitettu lapsen metodilla)
    def rasvaprosentti(self):
        self.rasvaprosentti = fitness.lapsen_rasvaprosentti(
            self.bmi, self.ika, self.sukupuoli)
        return self.rasvaprosentti

# Testaa Kuntoilija ja JunioriKuntoilija-luokat
if __name__ == "__main__":
    # Luodaan olio luokasta Kuntoilija
    kuntoilija = Kuntoilija('Kalle Kuntoilija', 171, 65, 40, 1)
    print(kuntoilija.nimi, 'painaa', kuntoilija.paino, 'kg')
    print('Painoindeksi on ', kuntoilija.bmi)
    print('Rasvaprosentti on', kuntoilija.rasvaprosentti())
    # Luodaan olio luokasta JunioriKuntoilija
    juniorikuntoilija = JunioriKuntoilija('Aku', 171, 65, 16, 1)
    print(juniorikuntoilija.nimi, 'painaa', juniorikuntoilija.paino, 'kg')
    print('Painoindeksi on ', juniorikuntoilija.bmi)
    print('Rasvaprosentti on', juniorikuntoilija.rasvaprosentti())