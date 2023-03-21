# Get basic information about an athlete and create athlete objects
# With functions instead of class-methods
# -----

# Libraries and modules
import json # For saving athlete information
import kuntoilija
import questions_with_funcs as questions


# Enter information about an athlete
name = questions.ask_user_string('Nimi: ')
date_of_weighing = questions.ask_user_string('Punnituspäivä (vvvv-kk-pp): ')
weight = questions.ask_user_float('Kuinka paljon painat? (kg): ')
height = questions.ask_user_float('Kuinka pitkä olet? (cm): ')
age = questions.ask_user_int('Kuinka vanha olet? (v): ')
gender = questions.ask_user_int('Oletko nainen vai mies? (0/1): ')

while True:
    if gender != 0 and gender != 1:
        print("Error in input, use 0/1.")
        gender = questions.ask_user_int('Oletko nainen vai mies? (0/1): ')
    else:
        break

neck = questions.ask_user_float('Minkä kokoinen on kaulasi ympärys? (cm): ')
waist = questions.ask_user_float('Minkä kokoinen on vyötärösi ympärys? (cm): ')

if gender == 0:
    hips = questions.ask_user_float("Minkä kokoinen on lantiosi ympärys? (cm): ")
else:
    hips = 0

# Create an athlete object from Kuntoilija class
athlete = kuntoilija.Kuntoilija(name, height, weight, age, gender, date_of_weighing, waist, neck, hips)

# Print some information about the athlete
text_to_show = f'Terve {athlete.nimi}, painoindeksisi tänään on {athlete.bmi}.'
print(text_to_show)
fat_percentage = athlete.rasvaprosentti()
usa_fat_percentage = athlete.laske_usa_rasvaprosentti()

text_to_show = f"Suomalainen rasva-% on {fat_percentage} ja amerikkalainen on {usa_fat_percentage}."
print(text_to_show)

saveinfo = input('Tallennetaanko tiedot? (k/e) ')
if saveinfo.lower() == 'k':
    # Save athlete information to a file, multi-line json
    filename = athlete.nimi.lower().replace(' ', '_') + '.json'
    with open(filename, 'w') as f:
        json.dump(athlete.__dict__, f, indent=4)
    print('Tiedot tallennettu tiedostoon', filename)
else:
    print('Tietoja ei tallennettu.')


# Secondary way, save all athletes in one file
# Empty list for all athlete data
athlete_data = []
# A dictionary for single weighing of an athlete
athlete_data_row = {
    'nimi': athlete.nimi,
    'pituus': athlete.pituus,
    'paino': athlete.paino,
    'ika': athlete.ika,
    'sukupuoli': athlete.sukupuoli,
    'date_of_weighing': athlete.punnitus_paiva,
    'vyotaron_ymparys': athlete.vyotaron_ymparys,
    'kaulan_ymparys': athlete.kaulan_ymparys,
    'lantion_ymparys': athlete.lantion_ymparys,
    'bmi': athlete.bmi,
    'rasvaprosentti': athlete.rasvaprosentti,
    'usa_rasvaprosentti': athlete.usa_rasvaprosentti
}

# Add a new data row to athlete_data list
athlete_data.append(athlete_data_row)

# Save data to a file
with open('athlete_data.json', 'w') as f:
    json.dump(athlete_data, f, indent=4)