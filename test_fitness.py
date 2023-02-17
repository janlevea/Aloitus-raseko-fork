# FITNESS-MODULIN TESTIT
# ======================

# KIRJASTOJEN JA MODULIEN LATAUKSET
import fitness

def test_laske_bmi():
    assert fitness.laske_bmi(64.7, 170) == 22.4
    assert fitness.laske_bmi(104.4, 182) == 31.5
    assert fitness.laske_bmi(40, 170) == 13.8
    assert fitness.laske_bmi(100, 170) == 34.6

def test_aikuisen_rasvaprosentti():
    # Aikuisia miehiä
    assert fitness.aikuisen_rasvaprosentti(22.4, 20, 1) == 15.3
    assert fitness.aikuisen_rasvaprosentti(13.8, 40, 1) == 9.6
    assert fitness.aikuisen_rasvaprosentti(34.6, 70, 1) == 41.4

    # Aikuisia naisia
    assert fitness.aikuisen_rasvaprosentti(20.8, 20, 0) == 24.2
    assert fitness.aikuisen_rasvaprosentti(13.8, 40, 0) == 20.4
    assert fitness.aikuisen_rasvaprosentti(34.6, 60, 0) == 49.9

def test_lapsen_rasvaprosentti():
    # Pojat
    assert fitness.lapsen_rasvaprosentti(24.4, 14, 1) == 24.8

    # Tytöt
    assert fitness.lapsen_rasvaprosentti(24.4, 14, 0) == 28.4


def test_usa_rasvaprosentti_mies():
    assert fitness.usa_rasvaprosentti_mies(182, 100, 40) == 24.9
    assert fitness.usa_rasvaprosentti_mies(175, 90, 40) == 19.3
    assert fitness.usa_rasvaprosentti_mies(170, 80, 40) == 11.9
    assert fitness.usa_rasvaprosentti_mies(181, 105, 38) == 29.2
    assert fitness.usa_rasvaprosentti_mies(171, 91, 38) == 22.2


def test_usa_rasvaprosentti_nainen():
    assert fitness.usa_rasvaprosentti_nainen(170, 70, 37, 90) == 18.3
    assert fitness.usa_rasvaprosentti_nainen(180, 100, 40, 80) == 25.0
    assert fitness.usa_rasvaprosentti_nainen(175, 85, 39, 85) == 21.5
    assert fitness.usa_rasvaprosentti_nainen(168, 70, 38, 80) == 12.2
    assert fitness.usa_rasvaprosentti_nainen(182, 98, 42, 90) == 27.5