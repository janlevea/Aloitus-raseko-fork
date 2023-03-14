# Module for asking questions from console and converting answers to various datatypes
# -------------------------------------------------------------------------------------

# Libraries and modules

# Class definitions
class Question:
    """A class containing methods to ask questions on console
    and converting answers to various datatypes."""

    def __init__(self, question):
        """Initialize class"""
        self.question = question

    @staticmethod
    def ask_user_int(question, loop):
        """Asks a question and converts the answer to int

        Args:
            question (str): Question to ask (print on users screen)
            loop (bool): If True asks the question until able to convert it

        Returns:
            tuple: answer as int, error message, error code, detailed error
        """
        if loop == True:
            while True:
                answer_txt = input(question)

                # Try to convert input string to integer
                try:
                    answer = int(answer_txt)
                    result = (answer, 'OK', 0, 'Conversion successful')
                    break
                # If an exception occurs tell the user to check input and try again
                except Exception as e:
                    print('Virhe syöteessä, älä käytä yksiköitä.')
                    print(e)
                    result = (0, 'Error', 1, str(e))
        else:
            answer_txt = input(question)
            # Try to convert input string to integer
            try:
                answer = int(answer_txt)
                result = (answer, 'OK', 0, 'Conversion successful')
            # If an exception occurs tell the user, but don't ask again
            except Exception as e:
                print('Virhe syöteessä, älä käytä yksiköitä.')
                print(e)
                result = (0, 'Error', 1, str(e))
        return result

    @staticmethod
    def ask_user_float(question, loop):
        """Asks a question and converts the answer to a floating point number

        Args:
            question (str): Question to ask (print on users screen)
            loop (bool): If True asks the question until able to convert it

        Returns:
            tuple: answer as float, error message, error code, detailed error
        """
        if loop == True:
            while True:
                answer_txt = input(question)
                # If user enters ',' instead of '.' - convert it to '.'
                answer_txt = answer_txt.replace(',', '.')
                # Try to convert input string to float
                try:
                    answer = float(answer_txt)
                    result = (answer, 'OK', 0, 'Conversion successful')
                    break
                # If an exception occurs tell the user to check input and try again
                except Exception as e:
                    print('Virhe syöteessä, älä käytä yksiköitä.')
                    print(e)
                    result = (0, 'Error', 1, str(e))
        else:
            answer_txt = input(question)
            answer_txt = answer_txt.replace(',', '.')
            # Try to convert input string to float
            try:
                answer = float(answer_txt)
                result = (answer, 'OK', 0, 'Conversion successful')
            # If an exception occurs tell the user, but don't ask again
            except Exception as e:
                print('Virhe syöteessä, älä käytä yksiköitä.')
                print(e)
                result = (0, 'Error', 1, str(e))
        
        return result

    @staticmethod
    def ask_user_bool(question, loop):
        """Asks a question and converts the answer(y/n) to a boolean True/False

        Args:
            question (str): Question to ask (print on users screen)
            loop (bool): If True asks the question until able to convert it

        Returns:
            tuple: answer as boolean, error message, error code, detailed error
        """
        if loop == True:
            while True:
                answer_txt = input(question)
                # Try to convert input string to boolean
                try:
                    if answer_txt.lower() == "y":
                        answer = True
                        result = (answer, 'OK', 0, 'Conversion successful')
                        break
                    elif answer_txt.lower() == "n":
                        answer = False
                        result = (answer, 'OK', 0, 'Conversion successful')
                        break
                    else:
                        print('Error in input, use y/n.')
                        result = (0, 'Error', 1, 'Wrong input')
                # If an exception occurs tell the user to check input and try again
                except Exception as e:
                    print('Error in input, use y/n.')
                    print(e)
                    result = (0, 'Error', 1, str(e))
        else:
            answer_txt = input(question)
            # Try to convert input string to boolean
            try:
                if answer_txt.lower() == "y":
                    answer = True
                    result = (answer, 'OK', 0, 'Conversion successful')
                elif answer_txt.lower() == "n":
                    answer = False
                    result = (answer, 'OK', 0, 'Conversion successful')
                else:
                    print('Error in input, use y/n.')
                    result = (0, 'Error', 1, 'Wrong input')
            # If an exception occurs tell the user, but don't ask again
            except Exception as e:
                print('Error in input, use y/n.')
                print(e)
                result = (0, 'Error', 1, str(e))
        return result

    @staticmethod
    def ask_user_bool_custom(question, true_value, false_value, loop):
        """Asks a question and converts the answer(true_value/false_value) to a boolean True/False

        Args:
            question (str): Question to ask (print on users screen)
            loop (bool): If True asks the question until able to convert it

        Returns:
            tuple: answer as boolean, error message, error code, detailed error
        """
        # If loop argument is true use while loop until user inputs correct value
        prompt = f'{question} vastaa {true_value}/{false_value}: '
        if loop == True:
            while True:
                answer_txt = input(prompt)
                # Try to convert input string to boolean
                try:
                    if answer_txt.lower() == true_value.lower():
                        answer = True
                        result = (answer, 'OK', 0, 'Conversion successful')
                        break
                    elif answer_txt.lower() == false_value.lower():
                        answer = False
                        result = (answer, 'OK', 0, 'Conversion successful')
                        break
                    else:
                        print(f'Error in input, use {true_value}/{false_value}')
                        result = ('N/A', 'Error', 1, 'Unable to convert input to bool')
                # If an exception occurs tell the user to check input and try again
                except Exception as e:
                    print(f'Error in input, use {true_value}/{false_value}')
                    print(e)
                    result = ('N/A', 'Error', 1, str(e))
        else:
            answer_txt = input(prompt)
            # Try to convert input string to boolean
            try:
                if answer_txt.lower() == true_value.lower():
                    answer = True
                    result = (answer, 'OK', 0, 'Conversion successful')
                elif answer_txt.lower() == false_value.lower():
                    answer = False
                    result = (answer, 'OK', 0, 'Conversion successful')
                else:
                    print(f'Error in input, use {true_value}/{false_value}')
                    result = ('N/A', 'Error', 1, 'Unable to convert input to bool')
            # If an exception occurs tell the user, but don't ask again
            except Exception as e:
                print(f'Error in input, use {true_value}/{false_value}')
                print(e)
                result = ('N/A', 'Error', 1, str(e))

        return result

    @staticmethod
    def ask_user_string(question):
        """Asks a question and returns it as string

        Args:
            question (str): Question to ask (print on users screen)

        Returns:
            tuple: answer as string, error message, error code, detailed error
        """
        # Ask user the question and return answer as string
        answer_txt = input(question)
        result = (answer_txt, 'OK', 0, 'Input ok')
        return result

    # A method to ask a question and convert answer according to a dictionary
    @staticmethod
    def ask_user_dictionary(question, dictionary, loop):
        """Return a value based on dictionary

        Args:
            question (str): The question to be asked
            dictionary (dict): Possible answers in key-value-pairs
            loop (bool): If True asks the question until able to convert it

        Returns:
            tuple: answer in correct type, error message, error code, detailed error
        """
        if loop == True:
            while True:
                answer_txt = input(question)
                try:
                    value = dictionary[answer_txt]
                    result = (value, 'OK', 0, 'Conversion successful')
                    break
                except Exception as e:
                    result = ('N/A', 'Error', 1, str(e))
        else:
            answer_txt = input(question)
            try:
                value = dictionary[answer_txt]
                result = (value, 'OK', 0, 'Conversion successful')
            except Exception as e:
                result = ('N/A', 'Error', 1, str(e))
        
        return result

    @staticmethod
    def ask_user_gender(question, loop):
        """Asks a question and converts the answer to gender as number (0=Female, 1=Male)

        Args:
            question (str): Question to ask (print on users screen)
            loop (bool): If True asks the question until able to convert it

        Returns:
            tuple: answer in correct type, error message, error code, detailed error
        """

        # Accepted inputs
        male_inputs = (
            "1", "mies", "poika", "man", "male", "m"
        )
        female_inputs = (
            "0", "nainen", "tyttö", "woman", "female", "f", "n"
        )

        if loop == True:
            while True:
                answer_txt = input(question)
                answer_txt = answer_txt.lower()
                if answer_txt in male_inputs:
                    gender = 1  # Male
                    result = (gender, 'OK', 0, 'Conversion successful')
                    return result
                elif answer_txt in female_inputs:
                    gender = 0  # Female
                    result = (gender, 'OK', 0, 'Conversion successful')
                    return result
                else:
                    result = ('Unknown gender', 'Error', 1, 'Unable to convert input to gender')
                    result = (gender, 'OK', 0, 'Conversion successful')
                    return result
        else:
            answer_txt = input(question)
            answer_txt = answer_txt.lower()
            if answer_txt in male_inputs:
                gender = 1  # Male
                result = (gender, 'OK', 0, 'Conversion successful')
                return result
            elif answer_txt in female_inputs:
                gender = 0  # Female
                result = (gender, 'OK', 0, 'Conversion successful')
                return result
            else:
                print('Virhe syötteessä. Sukupuolta ei tunnistettu.')
                result = ('Unknown gender', 'Error', 1, 'Unable to convert input to gender')
                return result

if __name__ == "__main__":
    # Test:
    # question = Question("Yes or no? (Y/N): ")
    # answer_and_error = question.ask_user_bool_custom('Y', 'N', False)
    # print(answer_and_error)
    # response = answer_and_error[0]

    answer_and_error = Question.ask_user_string("Enter name: ")
    name = answer_and_error[0]

    answer_and_error = Question.ask_user_float("Enter height (cm): ", True)
    height = answer_and_error[0]

    answer_and_error = Question.ask_user_float("Enter weight (kg): ", True)
    weight = answer_and_error[0]

    answer_and_error = Question.ask_user_int("Enter age: ", True)
    age = answer_and_error[0]

    answer_and_error = Question.ask_user_int("Enter gender (1 = man, 0 = woman): ", True)
    gender = answer_and_error[0]

    gender_dictionary = {   
        '0': 0,
        'tyttö': 0,
        'nainen': 0,
        "woman": 0,
        "female": 0,
        "f": 0,
        "n": 0,

        '1': 1,
        'mies': 1,
        'poika': 1,
        'man': 1,
        'male': 1,
        'm': 1,
    }
    answer_and_error = Question.ask_user_dictionary("Sukupuoli: ", gender_dictionary, True)
    print(answer_and_error)

    answer_and_error = Question.ask_user_float("Enter waist circumference (cm): ", True)
    waist_circumference = answer_and_error[0]

    answer_and_error = Question.ask_user_float("Enter neck cicumference (cm): ", True)
    neck_circumference = answer_and_error[0]

    answer_and_error = Question.ask_user_float("Enter hip cicumference (cm): ", True)
    hip_circumference = answer_and_error[0]

    print(name, height, weight, age, gender, waist_circumference,
          neck_circumference, hip_circumference)