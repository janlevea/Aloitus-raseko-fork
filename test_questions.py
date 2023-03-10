# questions.py - tests
import questions

# Test if conversion to float works as expected
def test_ask_user_float(monkeypatch):
    user_input = '100.8'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Anna liukuluku: ')
    assert question.ask_user_float(False) == (100.8, 'OK', 0, "Conversion successful")

def test_ask_user_float2(monkeypatch):
    user_input = '100.8kg'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Anna liukuluku: ')
    assert question.ask_user_float(False) == (0, 'Error', 1, "could not convert string to float: '100.8kg'")

def test_ask_user_float3(monkeypatch):
    user_input = '1.5v'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Anna liukuluku: ')
    assert question.ask_user_float(False) == (0, 'Error', 1, "could not convert string to float: '1.5v'")

# Test new static ask_user_int
def test_ask_user_int(monkeypatch):
    user_input = '100'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    assert questions.Question.ask_user_int('Anna kokonaisluku: ', False) == (100, 'OK', 0, "Conversion successful")

# # Test if conversion to integer works as expected
# def test_ask_user_int(monkeypatch):
#     user_input = '100'
#     monkeypatch.setattr('builtins.input', lambda _: user_input)
#     question = questions.Question('Anna kokonaisluku: ')
#     assert question.ask_user_int(False) == (100, 'OK', 0, "Conversion successful")

# Test if conversion to boolean works as expected
def test_ask_user_bool(monkeypatch):
    user_input = 'Y'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Anna boolean: ')
    assert question.ask_user_bool(False) == (True, 'OK', 0, "Conversion successful")

# Test if conversion to boolean works as expected in alternative method
def test_ask_user_bool2(monkeypatch):
    user_input = 'K'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Anna kyllä/ei (K/E): ')
    assert question.ask_user_bool2('K', 'E', False) == (True, 'OK', 0, "Conversion successful")

def test_ask_user_bool2_2(monkeypatch):
    user_input = 'E'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Anna kyllä/ei (K/E): ')
    assert question.ask_user_bool2('K', 'E', False) == (False, 'OK', 0, "Conversion successful")

def test_ask_user_bool2_3(monkeypatch):
    user_input = 'y'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Anna kyllä/ei (K/E): ')
    assert question.ask_user_bool2('K', 'E', False) == ('N/A', 'Error', 1, 'Unable to convert input to bool')

"""
def test_kysy_nimi(monkeypatch): # argumenttina monkeypatch-moduli (venv - pytest - monkeypatch.py)
    syote = 'Calle' # Simuloitu käyttäjän syöte
    monkeypatch.setattr('builtins.input', lambda _: syote) # korvataan järjestelmän input() muuttujalla syote
    assert syotto.kysy_nimi() == syote # varsinainen testi, funktio palauttaa sille syötteenä annetun merkkijonon
"""