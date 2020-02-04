from random import randrange

symbol_hrace = "x"
symbol_pocitace = "o"
delka_pole = 20


def vyhodnot(herni_situace):
    if "xxx" in herni_situace:
        return "x"
    elif "ooo" in herni_situace:
        return "o"
    elif "-" not in herni_situace:
        return "!"
    return "-"


def tah(herni_pole, index_policka, symbol):
    """Vrátí herní pole s daným symbolem umístěným na danou pozici."""
    if index_policka == 0:
        return symbol + herni_pole[index_policka + 1:]
    if index_policka == delka_pole - 1:
        return herni_pole[:index_policka] + symbol
    return herni_pole[:index_policka] + symbol + herni_pole[index_policka + 1:]


def tah_hrace(herni_pole):
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


def tah_pocitace(herni_pole):
    """Zahraje tah počítače - vyplní odpovídající symbol na vyhovující místo"""
    while True:
        index_policka = randrange(0, delka_pole - 1)
        if herni_pole[index_policka] == '-':
            break
    return tah(herni_pole, index_policka, symbol_pocitace)


def mozna_konec(herni_pole):
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
    herni_pole = '-' * delka_pole
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
