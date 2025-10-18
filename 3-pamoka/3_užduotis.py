"""
Užduotis: Jonuko problema

Jonukas žino, kad mokytoja jam gali duoti spręsti vieną iš trijų kontrolinio darbo variantų.
Atlikdamas užduotį jis gaus du skaičius a ir b, o jam reikės apskaičiuoti x reikšmę pagal vieną iš
trijų formulių.

Pirmas variantas: x = ab + 3;
Antras variantas: x = 2a + b;
Trečias variantas: x = a - 3b.

Parašykite programą, kuri padėtų Jonukui pasitikrinti, ar jis teisingai skaičiuoja x reikšmę
spręsdamas kiekvieno varianto užduotį.

Duomenys                                Rezultatai
Įveskite užduoties variantą 1           Atsakymas: x = 13
Įveskite a reikšmę 5
Įveskite b reikšmę 2

Įveskite užduoties variantą 2           Atsakymas: x = 12
Įveskite a reikšmę 5
Įveskite b reikšmę 2

Įveskite užduoties variantą 3           Atsakymas: x = -1
Įveskite a reikšmę 5
Įveskite b reikšmę 2
"""

# Rašyk savo kodą žemiau 👇

def get_var(v):
    if v == 1:
        return a * b + 3
    elif v == 2:
        return 2 * a + b
    elif v == 3:
        return a - 3 * b
global a, b
var=int(input("Iveskite uzduoties varianta (1, 2 arba 3): "))
a=int(input("Iveskite a reiksme: "))
b=int(input("Iveskite b reiksme: "))
print(f"Atsakymas: x = {get_var(var)}")
