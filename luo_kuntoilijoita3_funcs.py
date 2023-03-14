# TODO: Tee tämä tiedosto
# Alla luo_kuntoilijoita2.py koodi

# Get basic information about an athlete and create athlete objects
# -----

# Libraries and modules
import kuntoilija
import questions
import json # For saving athlete information


# Enter information about an athlete
name = input('Nimi: ')
# Ask details about her/him
question = questions.Question('Kuinka paljon painat? (kg): ')
weight = question.ask_user_float(True)[0]
question = questions.Question("Kuinka pitkä olet? (cm): ")
height = question.ask_user_float(True)[0]
question = questions.Question("Kuinka vanha olet? (v): ")
age =  question.ask_user_int(True)[0]

question = questions.Question("Oletko nainen vai mies? (0/1): ") 
gender = question.ask_user_int(True)[0]
while True:
    if gender != 0 or gender != 1:
        print("Error in input, use 0/1.")
        gender = question.ask_user_int(True)[0]
    else:
        break

question = questions.Question("Minkä kokoinen on kaulasi ympärys? (cm): ")
neck = question.ask_user_float(True)[0]
question = questions.Question("Minkä kokoinen on vyötärösi ympärys? (cm): ")
waist = question.ask_user_float(True) [0]

if gender == 0:
    question = questions.Question("Minkä kokoinen on lantiosi ympärys? (cm): ")
    hips = question.ask_user_float(True)[0]
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
