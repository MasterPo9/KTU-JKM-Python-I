def vaisiai():
    with open("vaisiai.txt", "r") as f:
        text = [i.strip()+" yra skanus\n" for i in f.readlines()]
    with open("rezultatas.txt", "w") as f:
        f.writelines(text)

def didziausias_skaitcius():
    with open("skaiciai.txt", "r") as f:
        skaiciai = [int(i.strip()) for i in f.readlines()]
    with open("rezultatas.txt", "w") as f:
        f.writelines(f"Didziausias skaicius: {max(skaiciai)}\nMaziausias skaicius: {min(skaiciai)}")

def fitr():
    with open("skaiciai2.txt", "r") as f:
        skaiciai = [i for i in f.readlines() if 5 <= int(i) <= 15]
    with open("rezultatas.txt", "w") as f:
        f.writelines(skaiciai)

def robot():
    with open("gamintojai.txt", "r") as f:
        rasti_gamintojai = [i for i in f.readlines() if i.lower().startswith("y")]
    with open("rezultatas.txt", "w") as f:
        f.writelines(f"Rasti {len(rasti_gamintojai)} gamintojai:\n\n")
        f.writelines(rasti_gamintojai)

def skaiciu_sumos():
    with open("skaiciai3.txt", "r") as f:
        skaiciai = [str(sum(y))+"\n" for y in [map(int, i.strip().split()) for i in f.readlines()]]
    with open("rezultatas.txt", "w") as f:
        f.writelines(skaiciai)

def teksto_analize():
    with open("zodziai.txt", "r") as f:
        zodziai = [str(i).upper() for i in f.readlines() if len(i.strip()) >= 4]
    with open("rezultatas.txt", "w") as f:
        f.writelines(zodziai)

def duomenu_validacija():
    with open("vartotojai.txt", "r") as f:
        vartotojai = [i.strip().split(",") for i in f.readlines()]
        galimi_vartotojai = [y[0]+"\n" for y in vartotojai if int(y[1]) >= 18]
    with open("rezultatas.txt", "w") as f:
        f.writelines(galimi_vartotojai)

def unikalios_reiksmes():
    with open("zodziai2.txt", "r") as f:
        zodziai = [i for i in f.readlines()]
    unikalus_zodziai = []
    for i in zodziai:
        if i not in unikalus_zodziai:
            unikalus_zodziai.append(i)
    unikalus_zodziai.sort(reverse=True)
    with open("rezultatas.txt", "w") as f:
        f.writelines(unikalus_zodziai)

def beganti_suma():
    with open("zodziai3.txt", "r") as f:
        skaiciai = f.readlines()
    suma = 0
    skaiciu_sumos=[]
    for i in skaiciai:
        suma += int(i.strip())
        skaiciu_sumos.append(str(suma)+"\n")
    with open("rezultatas.txt", "w") as f:
        f.writelines(skaiciu_sumos)

def veliaveles():
    with open("veleveles.txt", "r") as f:
        tekstas = [i.strip().split() for i in f.readlines()]
    raudona, geltona, zalia = 0, 0, 0
    for i in tekstas:
        if i[0] == "R":
            raudona += int(i[1])
        if i[0] == "G":
            geltona += int(i[1])
        if i[0] == "Z":
            zalia += int(i[1])
    veleveliu_skaicius = min([raudona, geltona, zalia])//2
    zalia -= veleveliu_skaicius*2
    geltona -= veleveliu_skaicius*2
    raudona -= veleveliu_skaicius*2
    with open("rezultatas.txt", "w") as f:
        f.writelines(f"Padarytas veliaveliu kiekis: {veleveliu_skaicius}\nG = {geltona}\nZ = {zalia}\nR = {raudona}\n")

veliaveles()