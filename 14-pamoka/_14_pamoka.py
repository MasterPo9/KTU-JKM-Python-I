

def salys():
    salys = {}
    with open("salys.txt", "r") as f:
        for i in f.readlines():
            salys[i.strip()] = "Nezinoma\n"

    with open("rezultatai.txt", "w") as f:
        for i in salys:
            f.write(f"{i} - {salys[i]}")

def salys2():
    salys = {}
    with open("salys2.txt", "r") as f:
        for i in f.readlines():
            salys[i.strip().split()[0]] = i.strip().split()[1]

    with open("rezultatai.txt", "w") as f:
        for i in salys:
            f.write(f"{i} - {salys[i]}\n")

def produktai():
    produktai = {}
    with open("produktai.txt", "r") as f:
        for i in f.readlines():
            if int(i.strip().split()[1]) > 5:
                produktai[i.strip().split()[0]] = i.strip().split()[1]

    with open("rezultatai.txt", "w") as f:
        for i in produktai:
            f.write(f"{i} - {produktai[i]}\n")
def gyventojai():
    gyventojai = {}
    with open("gyventojai.txt", "r") as f:
        for i in f.readlines():
            miestas, kiekis = i.strip().split()
            gyventojai[miestas] = int(kiekis)

    with open("rezultatai.txt", "w") as f:
        f.write(max(gyventojai.items())[0])
def vidurkis():
    vidurkiai = {}
    with open("pazymiai.txt", "r") as f:
        for i in f.readlines():
            vardas = i.strip().split()[0]
            pazymiai = list(map(int, i.strip().split()[1].split(",")))
            vidurkiai[vardas] = sum(pazymiai)/len(pazymiai)

    with open("rezultatai.txt", "w") as f:
        for i in vidurkiai:
            f.write(f"{i} - {vidurkiai[i]:.1f}\n")
def atvirkstinis_zodynas():
    pazymiai = {}
    with open("pazymiai2.txt", "r") as f:
        for i in f.readlines():
            mokinys, pazimys = i.strip().split()
            if pazimys not in pazymiai.keys():
                pazymiai[pazimys] = mokinys
            else:
                pazymiai[pazimys] += ","+mokinys

    with open("rezultatai.txt", "w") as f:
        for i in pazymiai:
            f.write(f"{i} - {pazymiai[i]}\n")
def duomenu_validacija():
    duomenys = {}
    with open("vartotojai.txt", "r") as f:
        for i in f.readlines():
            vartotojas = i.strip().split()
            pazymiai = list(map(int, vartotojas[1:]))
            duomenys[vartotojas[0]] = sum(pazymiai)/len(pazymiai)

    geriausias_mokinys = max(duomenys.items(), key=lambda x: x[1])[0]
    silpniausias_mokinys = min(duomenys.items(), key=lambda x: x[1])[0]

    vidurkiu_suma = 0
    for i in duomenys.values():
        vidurkiu_suma += i
    klases_vidurkis = vidurkiu_suma / len(duomenys)

    with open("rezultatai.txt", "w") as f:
        for i in duomenys:
            f.write(f"{i} - vidurkis: {duomenys[i]:.2f}\n")
        f.write(f"\nGeriausias mokinys: {geriausias_mokinys}\n")
        f.write(f"Silpniausias mokinys: {silpniausias_mokinys}\n")
        f.write(f"Klases vidurkis: {klases_vidurkis:.2f}\n")
