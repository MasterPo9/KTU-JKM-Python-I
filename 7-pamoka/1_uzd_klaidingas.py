# 💣💥⚠️ !!! DĖMESIO !!! KLAIDINGAI IŠSPRĘSTAS UŽDAVINYS !!! PATAISYK !!! ⚠️💥💣

"""
Sąlyga:

Vartotojas įveda kelis skaičius vienoje eilutėje (atskirtus tarpais).

Programa turi:
• išskirti lyginių skaičių sumą,
• suskaičiuoti nelyginių skaičių kiekį,
• rasti didžiausią ir mažiausią skaičių sąraše
"""

import m9_utils as utils

skaiciai = utils.cinput("Įveskite kelis skaičius: ", True)

lyginiu_suma = 0
nelyginiu_kiekis = 0

for i in range(0, len(skaiciai)):
    if skaiciai[i] % 2 == 0:
        lyginiu_suma += i
    elif skaiciai[i] % 2 == 1:
        nelyginiu_kiekis += 1

didziausias = max(skaiciai)
maziausias = min(skaiciai)

print("Lyginių skaičių suma yra:", lyginiu_suma)
print("Nelyginių skaičių kiekis yra:", nelyginiu_kiekis)
print("Mažiausias skaičius:", maziausias)
print("Didžiausias skaičius:", didziausias)