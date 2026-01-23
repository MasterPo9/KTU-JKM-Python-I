# doing backwards lol

import random

import m9_utils as utils
from m9_utils.trying_ani import BLUE, LIGHT_GREEN, GREEN, PURPLEC, BLINK, RED, REDBG, RESET


def v20(rng=False):
    pasleptas_zodis = "python"
    if rng:
        zodziai = ["morka", "python", "windows", "obuolys", "kompiuteris", "agurkai", "pomidorai"]
        pasleptas_zodis = random.choice(zodziai)

    raides = list(pasleptas_zodis)
    random.shuffle(raides)
    sumaisytas = "".join(raides)
    print(f"Sumaisytas zodis: {sumaisytas}")
    print(
        f"{f'{LIGHT_GREEN}Teisingas spejimas!{RESET}' if pasleptas_zodis == str(input('Jusu spejimas: ')) else f'{RED}Neteisingas Spejimas!{RESET}'}")


def v19():
    skaiciai = utils.cinput("Skaiciai: ", True, True)
    vid = sum(skaiciai) / len(skaiciai)
    did, maz = [], []
    for i in skaiciai:
        if i > vid:
            did.append(i)
        else:
            maz.append(i)

    print(f"Vidurkis: {vid}\nSkaiciai didesni uz vidurki : {did}\nSkaiciai mazesni uz vidurki: {maz}")

def v18():
    ivestis = utils.cinput("Ivestis: ")
    no_repeat = []
    for i in ivestis:
        if i not in no_repeat:
            no_repeat.append(i)
    print(f"Unikalus zodziai: {no_repeat}")

def v17():
    rib_maz = int(input("Iveskite maziausia riba: "))
    rib_did = int(input("Iveskite didziausia riba: "))
    ivestis = utils.cinput("Iveskite Skaicius: ", True, True, VIR = range(rib_maz, rib_did + 1), RNPL = True)
    vid = sum(ivestis[0]) / len(ivestis[0])
    print(f"Originalus sarasas: {ivestis[1]}\nFiltruoti skaiciai tarp {rib_maz} ir {rib_did}: {ivestis[0]}\nVidurkis: {vid}")

def v15():
    ivestis = input("Ivestis: ")
    raides=[]
    info = {}
    used = []
    raides.extend(ivestis)
    for i in raides:
        if i not in used:
            info.update({i: raides.count(i)})
            used.append(i)

    print(info)

def v14():
    preke1 = utils.cinput("Preke: ")
    preke2 = utils.cinput("Preke: ")
    preke3 = utils.cinput("Preke: ")
    preke4 = utils.cinput("Preke: ")
    preke5 = utils.cinput("Preke: ")
    prekes = [preke1[0], preke2[0], preke3[0], preke4[0], preke5[0]]
    kainos = [float(preke1[2]), float(preke2[2]), float(preke3[2]), float(preke4[2]), float(preke5[2])]
    bpreke = prekes[kainos.index(max(kainos))]
    print(f"Brangiausia preke: {bpreke}({max(kainos)})\nBendra Suma: {sum(kainos)}\nIlgiausias pavadinimas: {max(prekes, key=len)}")

def v13():
    tekstas = utils.cinput("Iveskite teksta: ")
    trumpi, vidutiniai, ilgi=[], [], []
    for i in tekstas:
        if len(i) <= 3:
            trumpi.append(i)
        if 6 >= len(i) >= 4:
            vidutiniai.append(i)
        if len(i)>6:
            ilgi.append(i)
    print(f"Ilgi: {ilgi}\nVidutiniai: {vidutiniai}\nTrumpi: {trumpi}")

def v12():
    number = random.randrange(1, 100)
    di=False
    for i in range(5):
        spejimas = int(input("Iveskite spejima: "))
        if spejimas == number:
            print(f"{GREEN}Atspejote!{RESET}")
            di=True
            break
        if spejimas > number:
            print(f"{BLUE}Per daug!{RESET}")
        if spejimas < number:
            print(f"{PURPLEC}Per mazai!{RESET}")
    if not di: print(f"{REDBG}{BLINK}Neatspejote!{RESET}")


v15()
