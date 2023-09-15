import sys
import re
from datetime import datetime
import time


def blad():
    print("BLAD")


def podzial_na_zmienne(wejscie):
    try:
        rejestracja, rodzaj_pojazdu, odleglosc, wjazd, wyjazd = wejscie.split(' ')
        return rejestracja, rodzaj_pojazdu, odleglosc, wjazd, wyjazd
    except:

        rejestracja = ""
        rodzaj_pojazdu = ""
        odleglosc = ""
        wjazd = ""
        wyjazd = ""
        return rejestracja, rodzaj_pojazdu, odleglosc, wjazd, wyjazd


def sprawdzenie_rejestracja(rej):
    if len(rej) != 6:
        return False
    test_liter = rej[:2]
    test_cyfr = rej[2:]
    czy_litery = test_liter.isalpha()
    czy_duze = test_liter.isupper()
    czy_cyfry = test_cyfr.isdigit()

    if czy_litery == False:
        return False
    elif czy_duze == False:
        return False
    elif czy_cyfry == False:
        return False
    else:
        return True


def sprawdzenie_czy_pojazd(pojazd):
    if len(pojazd) != 1:
        return False
    elif pojazd != "S" and pojazd != "C":
        return False
    else:
        return True


def sprawdzanie_czy_poprawna_odleglosc(dyst):
    if dyst.isdigit() == True:
        return True
    else:
        return False


def sprawdzenie_czy_poprawny_czas(czas):
    wzorzec_czasu = '^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$'
    sprawdzenie = re.findall(wzorzec_czasu, czas)
    if not sprawdzenie:
        return False
    else:
        return True


def obliczanie_sredniej_predkosci(czas_wjazdu, czas_wyjazdu, dystans):
    czas_wjazdu_time = datetime.strptime(czas_wjazdu.strip(), '%H:%M')
    czas_wyjazdu_time = datetime.strptime(czas_wyjazdu.strip(), '%H:%M')

    czas_przejazdu = (czas_wyjazdu_time - czas_wjazdu_time).seconds

    dystans_int = int(dystans)
    predkos_ms = dystans_int / czas_przejazdu
    predkosc_kmh = round(predkos_ms * (1 / 1000 * 3600), 2)

    return predkosc_kmh


def main():
    for linia_danych in sys.stdin:

        if linia_danych == '\n':
            blad()
            continue

        rejestracja, rodzaj_pojazdu, odleglosc, wjazd, wyjazd = podzial_na_zmienne(linia_danych)

        wynik_sprawdzenia_rejestracji = sprawdzenie_rejestracja(rejestracja)
        if wynik_sprawdzenia_rejestracji == False:
            blad()
            continue

        wynik_sprawdzenia_pojzadu = sprawdzenie_czy_pojazd(rodzaj_pojazdu)
        if wynik_sprawdzenia_pojzadu == False:
            blad()
            continue

        wynik_sprawdzania_odleglosci = sprawdzanie_czy_poprawna_odleglosc(odleglosc)
        if wynik_sprawdzania_odleglosci == False:
            blad()
            continue

        wynik_sprawdzenia_wjazdu = sprawdzenie_czy_poprawny_czas(wjazd)
        if wynik_sprawdzenia_wjazdu == False:
            blad()
            continue

        wynik_sprawdzenia_wyjazdu = sprawdzenie_czy_poprawny_czas(wyjazd)
        if wynik_sprawdzenia_wyjazdu == False:
            blad()
            continue

        srednia_predkosc = obliczanie_sredniej_predkosci(wjazd, wyjazd, odleglosc)

        kara = ""
        if rodzaj_pojazdu == "C" and srednia_predkosc > 80.00:
            kara = "M"
        elif rodzaj_pojazdu == "C" and srednia_predkosc <= 80.00:
            kara = "."
        elif rodzaj_pojazdu == "S" and srednia_predkosc > 120.00:
            kara = "M"
        elif rodzaj_pojazdu == "S" and srednia_predkosc <= 120.00:
            kara = "."

        print(rejestracja, kara, "%.2f" % srednia_predkosc)


if __name__ == '__main__':
    main()
