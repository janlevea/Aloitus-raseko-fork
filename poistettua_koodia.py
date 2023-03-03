# from luo_kuntoilijoita.py
def convert_input_to_float_or_int(which, input, which_input):
    """Convert user input to float or int

    Args:
        which (int): 0=float, 1=int
        input (string): string to convert
        which_input (string): what kind of input is it? (pituus, paino, ika, sukupuoli..)

    Returns:
        float/int: converted input
    """    
    try:
        if which == 0:
            input = float(input)
            return input
        elif which == 1:
            input = int(input)
            return input
        else:
            print("Error: which must be 0 or 1.")
            input == "ERROR"
            return input
    except Exception as e:
        print(e)
        print('Virheellinen syöte! Syötä', which_input, 'pelkkinä numeroina esim. 100')
        input = "ERROR"
        return input

# Loop until user gives a valid pituus(float) input
pituus = input('Anna pituus (cm): ')
float = convert_input_to_float_or_int(0, pituus, "pituus")
while True:
    if float == "ERROR":
        pituus = input('Anna pituus (cm): ')
        float = convert_input_to_float_or_int(0, pituus, "pituus")
    else:
        pituus = float
        break

# Loop until user gives a valid paino(float) input
paino = input('Anna paino (kg): ')
float = convert_input_to_float_or_int(0, paino, "paino")
while True:
    if float == "ERROR":
        paino = input('Anna paino (kg): ')
        float = convert_input_to_float_or_int(0, paino, "paino")
    else:
        paino = float
        break
        
# Loop until user gives a valid ika(int) input
while True:
    ika = input('Anna ikä: ')
    try:
        ika = int(ika)
        break
    except Exception as e:
        print(e)
        print('Virheellinen syöte! Syötä ikä pelkkinä numeroina.')
        pituus = input('Anna ikä: ')

# Loop until user gives a valid sukupuoli(int) input
while True:
    sukupuoli = input('Anna sukupuoli (1 = mies, 0 = nainen): ')
    try:
        sukupuoli = int(sukupuoli)
        break
    except Exception as e:
        print(e)
        print('Virheellinen syöte! Syötä sukupuoli pelkkänä numerona.')
        sukupuoli = input('Anna sukupuoli (1 = mies, 0 = nainen): ')

# Loop until user gives a valid vyotaron_ymparys(float) input
while True:
    vyotaron_ymparys = input('Anna vyötärön ympärysmitta (cm): ')
    try:
        vyotaron_ymparys = float(vyotaron_ymparys)
        break
    except Exception as e:
        print(e)
        print('Virheellinen syöte! Syötä vyotarön ympärys pelkkinä numeroina.')
        vyotaron_ymparys = input('Anna vyötärön ympärysmitta (cm): ')

# Loop until user gives a valid kaulan_ymparys(float) input
while True:
    kaulan_ymparys = input('Anna kaulan ympärysmitta (cm): ')
    try:
        kaulan_ymparys = float(kaulan_ymparys)
        break
    except Exception as e:
        print(e)
        print('Virheellinen syöte! Syötä kaulan ympärys pelkkinä numeroina.')
        kaulan_ymparys = input('Anna kaulan ympärysmitta (cm): ')

# Loop until user gives a valid kaulan_ymparys(float) input
while True:
    lantion_ymparys = input('Anna lantion ympärysmitta (cm): ')
    try:
        lantion_ymparys = float(lantion_ymparys)
        break
    except Exception as e:
        print(e)
        print('Virheellinen syöte! Syötä lantion ympärys pelkkinä numeroina.')
        lantion_ymparys = input('Anna lantion ympärysmitta (cm): ')