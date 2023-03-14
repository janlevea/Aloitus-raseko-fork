# questions.py - tests
import questions_with_funcs as questions

# Tests without raised exceptions:

# Test if conversion to integer works as expected
def test_ask_user_int(monkeypatch):
    user_input = '120'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.ask_user_int('Anna kokonaisluku: ')
    assert question == 120

# Test if conversion to float works as expected
def test_ask_user_float(monkeypatch):
    user_input = '120,5'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.ask_user_float('Anna liukuluku: ')
    assert question == 120.5

def test_ask_user_float2(monkeypatch):
    user_input = '122.5'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.ask_user_float('Anna liukuluku: ')
    assert question == 122.5

# Test if conversion to boolean works as expected
def test_ask_user_bool(monkeypatch):
    user_input = 'y'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.ask_user_bool("Enter yes(y) or no(n): ")
    assert question == True

def test_ask_user_bool2(monkeypatch):
    user_input = 'n'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.ask_user_bool("Enter yes(y) or no(n): ")
    assert question == False

# Test if conversion to boolean(custom) works as expected
def test_ask_user_bool_custom(monkeypatch):
    user_input = 'k'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.ask_user_bool_custom("Vastaa kyllä(k) or ei(e): ", "k", "e")
    assert question == True

def test_ask_user_bool_custom2(monkeypatch):
    user_input = 'e'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.ask_user_bool_custom("Vastaa kyllä(k) or ei(e): ", "k", "e")
    assert question == False

# Test if asking a string works as expected
def test_ask_user_string(monkeypatch):
    user_input = "Jani"
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.ask_user_string("Anna nimi: ")
    assert question == "Jani"


# TODO: Testejä joissa nostetaan virheitä (onko mahdollista koska While: True looppi?)