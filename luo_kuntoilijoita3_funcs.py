# Get basic information about an athlete and create athlete objects
# With functions instead of class-methods
# -----

# Libraries and modules
import kuntoilija
import questions_with_funcs as questions
import json # For saving athlete information


# Enter information about an athlete
name = questions.ask_user_string('Nimi: ')
weight = questions.ask_user_float('Kuinka paljon painat? (kg): ')
height = questions.ask_user_float('Kuinka pitkä olet? (cm): ')
age = questions.ask_user_int('Kuinka vanha olet? (v): ')
gender = questions.ask_user_int('Oletko nainen vai mies? (0/1): ')

while True:
    if gender != 0 or gender != 1:
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
athlete = kuntoilija.Kuntoilija(name, height, weight, age, gender, waist, neck, hips)

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
