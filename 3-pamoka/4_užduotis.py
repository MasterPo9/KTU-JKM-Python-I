"""
Užduotis: Skaičiai

Per matematikos pamoką teko nustatyti, kurie iš duotųjų teigiamų skaičių a, b ir c yra skaičiaus trys
(3) kartotiniai. Jei yra keli, reikia išvesti pirmą rastą, jeigu nėra nei vieno, reikia išvesti - nėra.

Parašykite programą, sprendžiančią šį uždavinį.

Duomenys                        Rezultatai
Įveskite a reikšmę 5            Atsakymas: 3
Įveskite b reikšmę 2
Įveskite c reikšmę 3

Įveskite a reikšmę 6            Atsakymas: 6
Įveskite b reikšmę 3
Įveskite c reikšmę 7

Įveskite a reikšmę 1            Atsakymas: nėra
Įveskite b reikšmę 2
Įveskite c reikšmę 5
"""

# Rašyk savo kodą žemiau 👇

a=int(input("Iveskite a reiksme: "))
b=int(input("Iveskite b reiksme: "))
c=int(input("Iveskite c reiksme: "))
if a % 3 == 0 or b % 3 == 0 or c % 3 == 0:
    if a % 3 == 0:
        print(f"Atsakymas: {a}")
    elif b % 3 == 0:
        print(f"Atsakymas: {b}")
    else:
        print(f"Atsakymas: {c}")
else:
    print("Atsakymas: nera")