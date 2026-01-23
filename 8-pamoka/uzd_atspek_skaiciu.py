"""
Užduotis: Atspėk skaičių

Sąlyga:
    Kompiuteris pasirenka atsitiktinį skaičių 0 - 10.
    Vartotojas spėja tol, kol atspėja.
    Programa turi:
        a) nurodyti, ar spėjimas per didelis ar per mažas;
        b) jei įvesta ne skaičius arba skaičius už 0 - 10 ribų - prašyti įvesti iš naujo;
        c) už kiekvieną neatspėtą kartą skaičiuoti baudas dvigubai:
           1-as neatspėjimas - 1 bauda, 2-as - 2 baudos, 3-ias - 4, ir t. t.;
        d) apskaičiuoti galutinius taškus = (100 // bandymai) - baudos.
           Galutiniai taškai negali būti neigiami!

Pavyzdys:
    Spėk skaičių: 5
    Deja, skaičius yra didesnis.
    Spėk skaičių: 9
    Deja, skaičius yra mažesnis.
    Spėk skaičių: 7
    Atspėjai per 3 kartus!
    Tavo taškai: 17
"""

import random

import m9_utils as utils

# Kompiuterio sugalvotas skaičius tarp 0 ir 10
skaicius = random.randint(0, 10) 
inp = -1
bandymai = 1
baudos = 0
# Savo kodą rašyk čia
while inp != skaicius:
    inp=utils.cinput("Spėk skaičių: ", True, False, 1, True, False, "Jūs pateikėte per mažai skaičiu!", True, 3, "Jūs pateikėte per daug skaičių!", VIR=range(0, 11), BOVIRV=True)[0]
    if inp != skaicius:
        bandymai += 1
        if baudos==0:
            baudos = 1
        else:
            baudos += baudos*2
        if inp<skaicius:
            print(f"{utils.CYAN}Deja, skaičius yra didesnis.{utils.RESET}")
        elif inp>skaicius:
            print(f"{utils.RED}Deja, skaičius yra mažesnis.{utils.RESET}")

taskai = (100//bandymai) - baudos
print(
    f"{utils.GREEN}Atspėjai per {bandymai} kartus!{utils.RESET}\nTavo taškai: {utils.REDBG + utils.BLINK if taskai < -20 else '' + utils.RED if -20 <= taskai < 0 else '' + utils.LIGHT_RED if 0 < taskai < 15 else '' + utils.YELLOW if 15 <= taskai <= 40 else '' + utils.GREEN if taskai > 40 else ''}{taskai}")
