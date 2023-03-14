# Asks basic info about the athlete and creates athlete objects
# ---------

# Libraries and modules
import kuntoilija
import json # For saving athlete information

# Functions...
# Ask a question and convert to numeric
def ask_user(question, float_or_int=0):
    """Ask a question from user

    Args:
        question (string): question to ask
        float_or_int (int): 0=float, 1=int

    Returns:
        result (float/int): converted answer
    """
    while True:
        answer_txt = input(question)
        # result = (0, 'Error', 1, 'Temporary error message')

        # Try to convert input to numeric
        try:
            if float_or_int == 0:
                answer_txt = answer_txt.replace(',', '.')
                answer = float(answer_txt)
                result = (answer, 'OK', 0, 'Conversion successful')
                break
            elif float_or_int == 1:
                answer = int(answer_txt)
                result = (answer, 'OK', 0, 'Conversion successful')
                break
            else:
                print('ERROR: argument: float_or_int something else than 0/1.')
                result = (0, 'Error', 1, 'Argument error')
                raise Exception('Argument error')

        # If an error occurs tell the user to check
        except Exception as e:
            print('Virhe syötetyssä arvossa, älä käytä yksiköitä.')
            print('Vain numerot ja mahd. desimaalimerkki sallittuja.')
            print(e)
            result = (0, 'Error', 1, str(e))

    return result


# Enter information about an athlete
nimi = input('Anna nimi: ')

# Ask length
answer = ask_user('Anna pituus (cm): ', 0)
pituus = answer[0] # Read first element of returned tuple

# Ask weight
answer = ask_user('Anna paino (kg): ', 0)
paino = answer[0]

# Ask age
answer = ask_user('Anna ikä: ', 1)
ika = answer[0]

# Ask gender
answer = ask_user('Anna sukupuoli (1 = mies, 0 = nainen): ', 1)
sukupuoli = answer[0]

# Ask waist circumference
answer = ask_user('Anna vyötärön ympärysmitta (cm): ', 0)
vyotaron_ymparys = answer[0]

# Ask neck circumference
answer = ask_user('Anna kaulan ympärysmitta (cm): ', 0)
kaulan_ymparys = answer[0]

# Ask hip circumference
answer = ask_user('Anna lantion ympärysmitta (cm): ', 0)
lantion_ymparys = answer[0]

print(nimi, pituus, paino, ika, 
    sukupuoli, vyotaron_ymparys, 
    kaulan_ymparys, lantion_ymparys)

athlete = kuntoilija.Kuntoilija(
    nimi, pituus, paino, ika, 
    sukupuoli, vyotaron_ymparys, 
    kaulan_ymparys, lantion_ymparys)

athlete.laske_usa_rasvaprosentti()
        
print(f"{athlete.nimi} painoindeksisi on {athlete.bmi}.")
if athlete.usa_rasvaprosentti > 0:
    print(f"USA rasvaprosenttisi = {athlete.usa_rasvaprosentti} %.")

saveinfo = input('Tallennetaanko tiedot? (k/e) ')
if saveinfo.lower() == 'k':
    # Save athlete information to a file, multi-line json
    filename = athlete.nimi.lower().replace(' ', '_') + '.json'
    with open(filename, 'w') as f:
        json.dump(athlete.__dict__, f, indent=4)
    print('Tiedot tallennettu tiedostoon', filename)
else:
    print('Tietoja ei tallennettu.')

print('Viimeisen kysymyksen virheilmoitus:', answer[1], 'koodi', answer[2], 'viesti(eng)', answer[3])