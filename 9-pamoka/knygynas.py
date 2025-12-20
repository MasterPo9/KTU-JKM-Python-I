"""
Užduotis: Knygynas „Lietuvių knygos“

Sąlyga:
    Duotas sąrašas „duomenys“, kuriame saugoma informacija apie knygas:
        autorius;pavadinimas;kaina
    Programa turi:
        1) Paprašyti vartotojo įvesti autoriaus vardą.
        2) Atspausdinti visas to autoriaus knygas (pavadinimą ir kainą).
        3) Suskaičiuoti, kiek knygų turi šis autorius.
        4) Suskaičiuoti bendrą visų knygų kainą.
        5) Jei autoriaus nėra, atspausdinti „Tokio autoriaus nėra“.

Pavyzdys:
    Įveskite autoriaus vardą: Aistis
    Vėjo ženklai 7.5
    Iš viso: 1

    Įveskite autoriaus vardą: Tomas
    Įvesto autoriaus 'Tomas' knygyne nerasta
"""

# Duomenys apie knygas
duomenys = [
    "Jablonskis;Lietuvos kalba;8.5",
    "Vaižgantas;Pragiedruliai;10.0",
    "Aistis;Vėjo ženklai;7.5",
    "Škėma;Balta drobulė;11.0",
    "Maironis;Pavasario balsai;9.0",
    "Šatrijos Ragana;Sename dvare;12.0",
    "Binkis;Laimės ženklai;6.5",
    "Baltakis;Miško paslaptys;7.0",
    "Zigmas;Dienoraštis;8.0",
    "Venclova;Tautos dainos;9.5"
]

# Savo kodą rašyk žemiau

vardas, pavadinimas, kaina = "", "", ""
vardai, pavadinimai, kainos = [], [], []
autorius = input("Iveskite autoriaus varda: ")
rastu_duomenu_kiekis = 0
for i in duomenys:
    vardas, pavadinimas, kaina = i.split(";")
    if str.lower(vardas) == str.lower(autorius):
        print(f"{pavadinimas} {kaina}")
        rastu_duomenu_kiekis += 1

if rastu_duomenu_kiekis > 0:
    print(f"Is viso: {rastu_duomenu_kiekis}")
else:
    print(f"Ivesto autoriaus '{autorius}' knygyne nerasta!")
