"""utf-8"""
from random import randrange

symbol_hrace = "x"
symbol_pocitace = "o"
symbol_pole = '-'
delka_pole = 20


def vyhodnot(herni_pole: str):
    if symbol_hrace * 3 in herni_pole:
        return "x"
    elif symbol_pocitace * 3 in herni_pole:
        return "o"
    elif symbol_pole not in herni_pole:
        return "!"
    return "-"


def tah(herni_pole: str, index_policka: int, symbol: str):
    """Vrátí herní pole s daným symbolem umístěným na danou pozici."""
    if index_policka == 0:
        return symbol + herni_pole[index_policka + 1:]
    if index_policka == delka_pole - 1:
        return herni_pole[:index_policka] + symbol
    return herni_pole[:index_policka] + symbol + herni_pole[index_policka + 1:]


def tah_hrace(herni_pole: str):
    """ Zeptá se hráče kam chcce hrát a vrátí změněné pole"""
    while True:
        index_policka = int(input("Kam chceš hrát? ")) - 1
        if index_policka > delka_pole - 1 or index_policka < 0:
            print("Takové políčko je mimo herní pole. Vyber jiné.")
        elif herni_pole[index_policka] == symbol_pocitace:
            print("Sem už hrál protihráč. Vyber jiné políčko.")
        elif herni_pole[index_policka] == symbol_hrace:
            print("Sem už jsi hrál. Vyber jiné políčko.")
        else:
            break
    return tah(herni_pole, index_policka, symbol_hrace)


def symboly_v_okoli(herni_pole: str, od_indexu: int, symbol: str, vzdalenost: int):
    vysledek = 0
    for i in range(1, vzdalenost + 1):
        if od_indexu + i > delka_pole - 1:
            break
        if herni_pole[od_indexu + i] != symbol:
            break
        vysledek = vysledek + 1
    for i in range(1, vzdalenost + 1):
        if od_indexu == 0:
            break
        if herni_pole[od_indexu - i] != symbol:
            break
        vysledek = vysledek + 1
    return vysledek


def hodnoceni_policka(herni_pole: str, index_policka: int):
    if herni_pole[index_policka] != symbol_pole:
        return 0
    elif symboly_v_okoli(herni_pole, index_policka, symbol_pocitace, 2) >= 2:
        return 7
    elif symboly_v_okoli(herni_pole, index_policka, symbol_hrace, 2) >= 2:
        return 6
    elif symboly_v_okoli(herni_pole, index_policka, symbol_pocitace, 1) == 1:
        if symboly_v_okoli(herni_pole, index_policka, symbol_pole, 1) == 1:
            return 5
        return 1
    elif symboly_v_okoli(herni_pole, index_policka, symbol_hrace, 1) == 1:
        return 4
    elif symboly_v_okoli(herni_pole, index_policka, symbol_pole, 2) >= 2:
        if index_policka != 0 and index_policka != delka_pole - 1:
            return 3
        else:
            return 2
    else:
        return 2


def tah_pocitace(herni_pole: str):
    """Zahraje tah počítače - vyplní odpovídající symbol na vyhovující místo"""
    seznam_policek = list(range(0, delka_pole))
    for i in range(0, delka_pole):
        seznam_policek[i] = hodnoceni_policka(herni_pole, i)
    index_policka = seznam_policek.index(max(seznam_policek))
    return tah(herni_pole, index_policka, symbol_pocitace)


def mozna_konec(herni_pole: str):
    vysledek = vyhodnot(herni_pole)
    if vysledek == symbol_hrace:
        print('Vyhrál jsi!')
        return True
    elif vysledek == symbol_pocitace:
        print('Prohrál jsi!')
        return True
    elif vysledek == '!':
        print('Je to remíza!')
        return True
    return False


def hra():
    herni_pole = symbol_pole * delka_pole
    while True:
        herni_pole = tah_hrace(herni_pole)
        print(herni_pole)
        if mozna_konec(herni_pole):
            break
        herni_pole = tah_pocitace(herni_pole)
        print('Hra počítače:')
        print(herni_pole)
        if mozna_konec(herni_pole):
            break
    print('Konec hry.')


hra()
