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
            loop (bool): If True asks the question until able to convert it

        Returns:
            tuple: answer as float, error message, error code, detailed error
        """
        if loop == True:
            while True:
                answer_txt = input(question)

                # Let's try to convert input to numeric
                try:
                    answer = int(answer_txt)
                    result = (answer, 'OK', 0, 'Conversion successful')
                    break
                # If an exception occurs tell the user to check
                except Exception as e:
                    print('Virhe syöteessä, älä käytä yksiköitä.')
                    print(e)
                    result = (0, 'Error', 1, str(e))
        else:
            answer_txt = input(question)
            # Let's try to convert input to numeric
            try:
                answer = int(answer_txt)
                result = (answer, 'OK', 0, 'Conversion successful')
            # If an exception occurs tell the user to check
            except Exception as e:
                print('Virhe syöteessä, älä käytä yksiköitä.')
                print(e)
                result = (0, 'Error', 1, str(e))
        return result


    def ask_user_float(self, loop):
        """Asks a question and converts the answer to a floating point number

        Args:
            loop (bool): If True asks the question until able to convert it

        Returns:
            tuple: answer as float, error message, error code, detailed error
        """
        if loop == True:
            while True:
                answer_txt = input(self.question)
                answer_txt = answer_txt.replace(',', '.')
                # Let's try to convert input to numeric
                try:
                    answer = float(answer_txt)
                    result = (answer, 'OK', 0, 'Conversion successful')
                    break
                # If an exception occurs tell the user to check
                except Exception as e:
                    print('Virhe syöteessä, älä käytä yksiköitä.')
                    print(e)
                    result = (0, 'Error', 1, str(e))
        else:
            answer_txt = input(self.question)
            answer_txt = answer_txt.replace(',', '.')
            # Let's try to convert input to numeric
            try:
                answer = float(answer_txt)
                result = (answer, 'OK', 0, 'Conversion successful')
            # If an exception occurs tell the user to check
            except Exception as e:
                print('Virhe syöteessä, älä käytä yksiköitä.')
                print(e)
                result = (0, 'Error', 1, str(e))
        
        return result

    # def ask_user_int(self, loop):
    #     """Asks a question and converts the answer to int

    #     Args:
    #         loop (bool): If True asks the question until able to convert it

    #     Returns:
    #         tuple: answer as float, error message, error code, detailed error
    #     """
    #     if loop == True:
    #         while True:
    #             answer_txt = input(self.question)

    #             # Let's try to convert input to numeric
    #             try:
    #                 answer = int(answer_txt)
    #                 result = (answer, 'OK', 0, 'Conversion successful')
    #                 break
    #             # If an exception occurs tell the user to check
    #             except Exception as e:
    #                 print('Virhe syöteessä, älä käytä yksiköitä.')
    #                 print(e)
    #                 result = (0, 'Error', 1, str(e))
    #     else:
    #         answer_txt = input(self.question)
    #         # Let's try to convert input to numeric
    #         try:
    #             answer = int(answer_txt)
    #             result = (answer, 'OK', 0, 'Conversion successful')
    #         # If an exception occurs tell the user to check
    #         except Exception as e:
    #             print('Virhe syöteessä, älä käytä yksiköitä.')
    #             print(e)
    #             result = (0, 'Error', 1, str(e))
    #     return result

    def ask_user_bool(self, loop):
        if loop == True:
            while True:
                answer_txt = input(self.question)
                # Try to convert input to boolean
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

                except Exception as e:
                    print('Error in input, use y/n.')
                    print(e)
                    result = (0, 'Error', 1, str(e))
        else:
            answer_txt = input(self.question)
            # Try to convert input to boolean
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
            # If an exception occurs tell the user to check
            except Exception as e:
                print('Error in input, use y/n.')
                print(e)
                result = (0, 'Error', 1, str(e))
        return result

    def ask_user_bool2(self, true_value, false_value, loop):
        # If loop argument is true use while loop until user inputs correct value
        prompt = f'{self.question} vastaa {true_value}/{false_value}: '
        if loop == True:
            while True:
                answer_txt = input(prompt)
                # Try to convert input to boolean
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
                except Exception as e:
                    print(f'Error in input, use {true_value}/{false_value}')
                    print(e)
                    result = ('N/A', 'Error', 1, str(e))
        else:
            answer_txt = input(prompt)
            # Try to convert input to boolean
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
            # If an exception occurs tell the user to check
            except Exception as e:
                print(f'Error in input, use {true_value}/{false_value}')
                print(e)
                result = ('N/A', 'Error', 1, str(e))

        return result

    def ask_user_string(self):
        """Asks a question and returns it as string

        Returns:
            str: result with debug info
        """
        answer_txt = input(self.question)
        result = (answer_txt, 'OK', 0, 'Input ok')
        return result

if __name__ == "__main__":
    # Test:
    # question = Question("Yes or no? (Y/N): ")
    # answer_and_error = question.ask_user_bool2('Y', 'N', False)
    # print(answer_and_error)
    # response = answer_and_error[0]

    question = Question("Enter name: ")
    answer_and_error = question.ask_user_string()
    name = answer_and_error[0]

    question = Question("Enter height (cm): ")
    answer_and_error = question.ask_user_float(True)
    height = answer_and_error[0]

    question = Question("Enter weight (kg): ")
    answer_and_error = question.ask_user_float(True)
    weight = answer_and_error[0]

    question = Question("Enter age: ")
    answer_and_error = question.ask_user_int(True)
    age = answer_and_error[0]

    question = Question("Enter gender (1 = man, 0 = woman): ")
    answer_and_error = question.ask_user_int(True)
    gender = answer_and_error[0]

    question = Question("Enter waist circumference (cm): ")
    answer_and_error = question.ask_user_float(True)
    waist_circumference = answer_and_error[0]

    question = Question("Enter neck cicumference (cm): ")
    answer_and_error = question.ask_user_float(True)
    neck_circumference = answer_and_error[0]

    question = Question("Enter hip cicumference (cm): ")
    answer_and_error = question.ask_user_float(True)
    hip_circumference = answer_and_error[0]

    print(name, height, weight, age, gender, waist_circumference,
          neck_circumference, hip_circumference)
