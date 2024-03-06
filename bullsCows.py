"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Monika Jelínková
email: jelinkova.monik@seznam.cz
discord: Mona_53888
"""

import random

def generovani_tajneho_cisla():
    prvni_cifra = random.randint(1, 9) #různá od nuly
    ostatni_cifry = random.sample(range(10), 3) #3 unikátní čísla 0-9
    return [prvni_cifra] + ostatni_cifry

def vysledek_hadani(tajne_cislo, tip):
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

def hadani():
    tip = input("Zadej svůj tip (4 čísla): ")
    hadani = []
    if len(tip) != 4:
        print("Zadané číslo nemá 4 cifry.")
        return
    elif tip.isnumeric() == False:
        print("Zadejte číslo!")
        return
    elif int(tip[0]) == 0:
        print("Hádané číslo nezačíná nulou.")
        return
    elif len(list(tip)) != len(list(set(tip))):
        print("Použil jsi duplicitně cifru")
        return
    else:
        for x in tip:
            hadani.append(int(x))
    return hadani

tajny_kod = generovani_tajneho_cisla()
print(tajny_kod)

while True:
            #hadani = [int(x) for x in input("Zadej svůj tip (4 čísla): ")]
            # hadani = []
            # for x in input("Zadej svůj tip (4 čísla): "):
            #     hadani.append(int(x))
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

        print(f"Vyhodnocení: {vyhodnoceni[0]} {bull}, {vyhodnoceni[1]} {cow}")

        if vyhodnoceni[0] == 4:
            print("Gratuluji! Podařilo se ti uhádnout tajný kód.")
            break
    else:
        continue
