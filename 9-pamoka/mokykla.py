"""
Užduotis: Mokiniai ir pažymiai

Sąlyga:
    Duotas sąrašas „mokykla“, kuriame saugoma informacija apie mokinius:
        kiekviena eilutė: vardas;pažymys
    Programa turi:
        1) Paprašyti vartotojo įvesti mokinio vardą.
        2) Atspausdinti visus to mokinio pažymius.
        3) Suskaičiuoti, kiek pažymių turi šis mokinys.
        4) Jei mokinio nėra, atspausdinti „Mokinys nerastas“.

Pavyzdys:
    Įveskite vardą: Jonas
    8
    10
    Iš viso: 2

    Įveskite vardą: Laura
    Mokinys Laura mokykloje nerastas
"""

# Duomenys apie mokinius            kodel cia du as esu nes :3
mokykla = ["Jonas;8", "Aistė;9", "Povilas;9", "Jonas;10", "Povilas;10"]

# Savo kodą rašyk žemiau

one_string_list = []

vardas = input("Iveskite varda: ")
pazymiai = []
neradimu_kiekis = 0
for i in mokykla:
    one_string_list = i.split(";")
    if one_string_list[0] == vardas:
        pazymiai.append(one_string_list[1])
        print(one_string_list[1])
if neradimu_kiekis == len(pazymiai):
    print(f"Mokinys {vardas} mokykloje nerastas")
    exit(404)

else: print(f"Is viso: {len(pazymiai)}")

# infostr = {}
#
# d2 = []
#
# for i in mokykla:
#     one_string_list = i.split(";")
#     d1, d2= one_string_list[0], list(one_string_list[1])
#     if d1 not in infostr:
#         infostr.update({d1: d2})
#     else:
#         od2=list(infostr.get(d1))
#         od2.append(d2)
#         infostr.update({d1: od2})
#
# print(infostr)
# got = infostr.get(vardas)
# print(got)
