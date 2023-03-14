# questions_staticmethods.py - tests
import questions_staticmethods as questions

# Tests without raised exceptions:

# Test if conversion to integer works as expected
def test_ask_user_int(monkeypatch):
    user_input = '120'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    answer = questions.Question.ask_user_int('Anna kokonaisluku: ', False)
    assert answer[0] == 120

# Test if conversion to float works as expected
def test_ask_user_float(monkeypatch):
    user_input = '120,5'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    answer = questions.Question.ask_user_float('Anna liukuluku: ', False)
    assert answer[0] == 120.5

def test_ask_user_float2(monkeypatch):
    user_input = '122.5'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    answer = questions.Question.ask_user_float('Anna liukuluku: ', False)
    assert answer[0] == 122.5

# Test if conversion to boolean works as expected
def test_ask_user_bool(monkeypatch):
    user_input = 'y'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    answer = questions.Question.ask_user_bool("Enter yes(y) or no(n): ", False)
    assert answer[0] == True

def test_ask_user_bool_custom(monkeypatch):
    user_input = 'n'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    answer = questions.Question.ask_user_bool("Enter yes(y) or no(n): ", False)
    assert answer[0] == False

# Test if conversion to boolean(custom) works as expected
def test_ask_user_bool_custom(monkeypatch):
    user_input = 'k'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    answer = questions.Question.ask_user_bool_custom("Vastaa kyllä(k) or ei(e): ", "k", "e", False)
    assert answer[0] == True

def test_ask_user_bool_custom2(monkeypatch):
    user_input = 'e'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    answer = questions.Question.ask_user_bool_custom("Vastaa kyllä(k) or ei(e): ", "k", "e", False)
    assert answer[0] == False

# Test if asking a string works as expected
def test_ask_user_string(monkeypatch):
    user_input = "Jani"
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    answer = questions.Question.ask_user_string("Anna nimi: ")
    assert answer[0] == "Jani"

# Test if asking a gender works as expected
def test_ask_user_gender(monkeypatch):
    user_input = "mies"
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    answer = questions.Question.ask_user_gender("Anna sukupuoli (0=Nainen/1=Mies): ", False)
    assert answer[0] == 1

def test_ask_user_gender2(monkeypatch):
    user_input = "nainen"
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    answer = questions.Question.ask_user_gender("Anna sukupuoli (0=Nainen/1=Mies): ", False)
    assert answer[0] == 0

def test_ask_user_gender3(monkeypatch):
    user_input = "1"
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    answer = questions.Question.ask_user_gender("Anna sukupuoli (0=Nainen/1=Mies): ", False)
    assert answer[0] == 1

def test_ask_user_gender4(monkeypatch):
    user_input = "0"
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    answer = questions.Question.ask_user_gender("Anna sukupuoli (0=Nainen/1=Mies): ", False)
    assert answer[0] == 0

def test_ask_user_gender5(monkeypatch):
    user_input = "man"
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    answer = questions.Question.ask_user_gender("Anna sukupuoli (0=Nainen/1=Mies): ", False)
    assert answer[0] == 1

def test_ask_user_gender6(monkeypatch):
    user_input = "woman"
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    answer = questions.Question.ask_user_gender("Anna sukupuoli (0=Nainen/1=Mies): ", False)
    assert answer[0] == 0

# Test to get value from dictionary
def test_ask_user_dictionary(monkeypatch):
    user_input = "tyttö"
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    user_input = user_input.lower()

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

    answer = questions.Question.ask_user_dictionary("Anna sukupuoli: ", gender_dictionary, False)
    assert answer[0] == 0

def test_ask_user_dictionary2(monkeypatch):
    user_input = "mies"
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    user_input = user_input.lower()

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
    
    answer = questions.Question.ask_user_dictionary("Anna sukupuoli: ", gender_dictionary, False)
    assert answer[0] == 1

# TODO: Testejä joissa nostetaan virheitä (onko mahdollista koska While: True looppi?)