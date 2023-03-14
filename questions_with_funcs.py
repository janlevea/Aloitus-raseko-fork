# Functions for asking questions from console and converting answers to various datatypes
# ----------

# Libraries and modules


# Function definitions
def ask_user_int(question):
    """Asks a question and converts the answer to int

    Args:
        question (str): Question to ask (print on users screen)

    Returns:
        int: answer as int
    """
    while True:
        answer_txt = input(question)

        # Let's try to convert input to numeric
        try:
            answer = int(answer_txt)
            return answer
        # If an exception occurs tell the user to check
        except Exception as e:
            print('Virhe syöteessä, älä käytä yksiköitä.')
            print(e)

def ask_user_float(question):
    """Asks a question and converts the answer to a floating point number

    Args:
        question (str): Question to ask (print on users screen)

    Returns:
        float: answer as float
    """
    while True:
        answer_txt = input(question)
        answer_txt = answer_txt.replace(',', '.')
        # Let's try to convert input to float
        try:
            answer = float(answer_txt)
            return answer
        # If an exception occurs tell the user to check
        except Exception as e:
            print('Virhe syöteessä, älä käytä yksiköitä.')
            print(e)

def ask_user_bool(question):
    """Asks yes(y) or no(n) and converts the answer to a boolean

    Args:
        question (str): Question to ask (print on users screen)
    Returns:
        bool: True/False
    """
    while True:
        answer_txt = input(question)
        # Try to convert input to boolean
        try:
            if answer_txt.lower() == "y":
                return True
            elif answer_txt.lower() == "n":
                return False
            else:
                print('Error in input, use y/n.')
        except Exception as e:
            print('Error in input, use y/n.')
            print(e)

def ask_user_bool_custom(question, true_value, false_value):
    prompt = f'{question} Vastaa {true_value}/{false_value}: '
    while True:
        answer_txt = input(prompt)
        # Try to convert input to boolean
        try:
            if answer_txt.lower() == true_value.lower():
                return True
            elif answer_txt.lower() == false_value.lower():
                return False
            else:
                print(f'Error in input, use {true_value}/{false_value}')
        except Exception as e:
            print(f'Error in input, use {true_value}/{false_value}')
            print(e)

def ask_user_string(question):
    """Asks a question and returns it as string

    Returns:
        str: answer
    """
    answer = input(question)
    return answer

def ask_user_gender(question):
    """Asks a question and converts the answer to gender as number (0=Female, 1=Male)

    Args:
        question (str): Question to ask (print on users screen)

    Returns:
        int: gender as int (0=Female/1=Male)
    """

    # Accepted inputs
    male_inputs = (
        "1", "mies", "poika", "man", "male", "m"
    )
    female_inputs = (
        "0", "nainen", "tyttö", "woman", "female", "f", "n"
    )

    while True:
        answer_txt = input(question)
        answer_txt = answer_txt.lower()
        if answer_txt in male_inputs:
            gender = 1  # Male
            return gender
        elif answer_txt in female_inputs:
            gender = 0  # Female
            return gender
        else:
            print('Virhe syötteessä. Sukupuolta ei tunnistettu.')

if __name__ == "__main__":
    name = ask_user_string("Enter name: ")
    height = ask_user_float("Enter height (cm): ")
    weight = ask_user_float("Enter weight (kg): ")
    age = ask_user_int("Enter age: ")
    # TODO: if answer "man" as string convert to 1 and "woman" to 0 (myös mies/nainen/male/female)
    gender = ask_user_int("Enter gender (1 = man, 0 = woman): ")
    waist = ask_user_float("Enter waist circumference (cm): ")
    neck = ask_user_float("Enter neck cicumference (cm): ")
    hip = ask_user_float("Enter hip cicumference (cm): ")

    if age == 0:
        gender_txt = "Female"
    elif age == 1:
        gender_txt = "Male"

    print(f'Name: {name} - Gender: {gender_txt} - Age: {age}y')
    print(f'Height: {height}cm - Weight: {weight}kg')
    print(f'Waist: {waist}cm - Neck: {neck}cm - Hip: {hip}cm')