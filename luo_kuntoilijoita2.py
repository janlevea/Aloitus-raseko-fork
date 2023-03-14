# Get basic information about an athlete and create athlete objects
# -----

# Libraries and modules
import kuntoilija
import questions

# Ask a question and convert the answer to float


# Enter information about an athlete
name = input('Nimi: ')

# Ask details about her/him
question = questions.Question('Kuinka paljon painat? (kg): ')
weight = question.ask_user_float(True)[0]
question = questions.Question("Kuinka pitkä olet? (cm): ")
height = question.ask_user_float(True)[0]
question = questions.Question("Kuinka vanha olet? (v): ")
age =  question.ask_user_int(True)[0]

# TODO: What if user responds integer other than 0/1? (it's not handled)
question = questions.Question("Oletko nainen vai mies? (0/1): ") 
gender = question.ask_user_int(True)[0]

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
usa_fat_percentage = athlete.usa_rasvaprosentti()

text_to_show = f"Suomalainen rasva-% on {fat_percentage} ja amerikkalainen on {usa_fat_percentage}."
print(text_to_show)

# TODO: Save user information to a file (json, tehty jo johonkin tiedostoon)