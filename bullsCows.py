"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Monika Jelínková
email: jelinkova.monik@seznam.cz
discord: Mona_53888
"""

import random

def generovani_tajneho_cisla():
    """
    Fce generuje tajné číslo - 1. cifra je různá od nuly a v čísle není žádná cifra vícekrát
    :return: list se 4 ciframi
    :rtype: list    
    """
    prvni_cifra = random.randint(1, 9) 
    ostatni_cifry = random.sample(list(set(range(10)).difference({prvni_cifra})), 3) 
    return [prvni_cifra] + ostatni_cifry

def hadani():
    """
    Fce ukládá tipovanou hodnotu hráče a ověřuje, zda odpovídá podmínkám:
    hodnota je 4ciferná, neobsahuje jiné znaky než číslice, na první pozici není nula
    a neobsahuje duplicitní číslice.
    """
    tip = input("Zadej svůj tip (4 čísla): ")
    hadani = []
    if len(tip) != 4:
        print("Zadané číslo nemá 4 cifry.")
        return
    elif tip.isnumeric() == False:
        print("Zadej číslo!")
        return 
    elif int(tip[0]) == 0:
        print("Hádané číslo nezačíná nulou.")
        return
    elif len(list(tip)) != len(list(set(tip))):
        print("Použil jsi duplicitně cifru")
        return
    else:
        hadani = [int(x) for x in tip]
    return hadani

def vysledek_hadani(tajne_cislo, tip):
    """
    Fce zazanamenává průběh hádání - porovnává zadanou hodnotu s tajným číslem 
    a vyhodnocuje, kolik bylo bull(s) a cow(s).

    :param tajne_cislo: výstup z fce generovani_tajneho_cisla()
    :param tip: výstup hadani z fce hadani()
    """
    bulls = 0
    cows = 0
    for i in range(4):
        if tip[i] == tajne_cislo[i]:
            bulls += 1
    for i in tip:
        if i in tajne_cislo:
            cows += 1
    cows = cows - bulls
    return bulls, cows

#výpis hry:
uvitani = """Vygenerovala jsem pro tebe 4místný tajný kód. 
Zahraj si hru bulls and cows!"""
print("-"*len(uvitani), "Ahoj!".center(len(uvitani)), "-"*len(uvitani), uvitani, "-"*len(uvitani), sep="\n")
tajny_kod = generovani_tajneho_cisla()
#print(tajny_kod)
pokus = 0
while True:
    pokus += 1
    tip = hadani()
    if tip:
        vyhodnoceni = vysledek_hadani(tajny_kod, tip)
        
        bull = ""
        if vyhodnoceni[0] == 1:
            bull = "bull"
        else:
            bull = "bulls"

        cow = ""
        if vyhodnoceni[1] == 1:
            cow = "cow"
        else:
            cow = "cows"


        print(f"Vyhodnocení: {vyhodnoceni[0]} {bull}, {vyhodnoceni[1]} {cow} \n {"-" * len(uvitani)}")

        if vyhodnoceni[0] == 4:
            print(f"Gratuluji! Podařilo se ti uhádnout tajný kód. Zvládl jsi to na {pokus}. pokus. \n {"-" * len(uvitani)}")
            break
    else:
        continue

