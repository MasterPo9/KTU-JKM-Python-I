"""
Užduotis: Automobilių parduotuvė „Greitasis ratas“

Sąlyga:
    Duotas sąrašas „automobiliai“, kuriame saugoma informacija apie automobilius:
        gamintojas;modelis;kaina

    Programa turi:
        1) Paprašyti vartotojo įvesti gamintojo vardą ir parodyti visus to gamintojo automobilius:
            - spausdinti modelį ir kainą;
            - suskaičiuoti, kiek automobilių to gamintojo yra;
            - jei gamintojo nėra, atspausdinti „Nurodyto gamintojo nėra“.

        2) Paprašyti vartotojo įvesti maksimalų biudžetą:
            - spausdinti visus automobilius, kurių kaina mažesnė arba lygi biudžetui;
            - suskaičiuoti, kiek automobilių atitiko kriterijų;
            - jei tokių automobilių nėra, atspausdinti „Nėra automobilių už <biudžetas> ar mažiau“.

        3) Parodyti pigiausią ar brangiausią automobilį vartotojo pasirinktam gamintojui:
            - atspausdinti tik kainą;
            - jei gamintojo nėra, atspausdinti „Tokio gamintojo nėra“.
"""

# Duomenys apie automobilius
automobiliai = [
    "Toyota;Corolla;15000",
    "BMW;X5;45000",
    "Honda;HR-V;50000",
    "Audi;A4;30000",
    "Toyota;Yaris;12000",
    "BMW;320i;28000",
    "Honda;CR-V;42000",
    "Audi;Q7;60000",
    "Honda;Civic;18000"
]

# Savo kodą rašyk žemiau

vardas, pavadinimas, kaina = "", "", ""
pavadinimai, kainos = [], []
gamintojas = input("Iveskite gamintojo varda: ")
rastu_duomenu_kiekis = 0

for i in automobiliai:
    vardas, pavadinimas, kaina = i.split(";")
    if str.lower(vardas) == str.lower(gamintojas):
        print(f"{pavadinimas} {kaina}")
        pavadinimai.append(pavadinimas)
        kainos.append(kaina)
        rastu_duomenu_kiekis += 1

if rastu_duomenu_kiekis > 0:
    print(f"Is viso: {rastu_duomenu_kiekis}")
else:
    print(f"Nurodyto gamintojo nera.")
    exit()

ct, rastu_duomenu_kiekis = 0, 0
budget = int(input("Iveskite biudzeta: "))
for i in pavadinimai:
    if int(kainos[ct]) <= budget:
        print(f"{i} {kainos[ct]}")
        rastu_duomenu_kiekis += 1
    ct += 1

if rastu_duomenu_kiekis > 0:
    print(f"Is viso: {rastu_duomenu_kiekis}")
else:
    print(f"Nera automobiliu uz {budget} ar maziau")
    exit()

mini, maxi = kainos.index(min(kainos)), kainos.index(max(kainos))
print(f"Maziausiai kainuojantis automobilis yra {pavadinimai[mini]}, kurio kaina yra {kainos[mini]}, o daugiausiai kainuojantis automobilis yra {pavadinimai[maxi]}, kurio kaina yra {kainos[maxi]}")