# Duomenų faile „Saldainiai.txt“ pateikta ši informacija:
# gamintojas, saldainių pavadinimas, turimas kiekis parduotuvėje, vieno kg kaina.
gamintojas = input("Iveskite saldainiu gamintojo pavadinima: ")
saldainiai = {}

with open("saldainiai.txt","r") as f:
    saldainiai_failas = [i.strip().split(";") for i in f.readlines()]
for i in saldainiai_failas:
    if i[0].lower() == gamintojas.lower():
         saldainiai[i[1]] = [i[1], i[2], i[3]]

if not saldainiai:
    print("Tokio gamintojo parduotuvė „Smaližius“ saldainiais neprekiauja")
    exit()
for p, k, v in saldainiai.values():
    print(f"{p}, turima {k}. Kainuoja {v} Eur per Kg.")
print(f"Iš viso yra {len(saldainiai)} saldainiai.")

kaina = float(input("Kokia didziausia Kg kaina? "))
saldainiai = {}
for i in saldainiai_failas:
    if float(i[3]) < kaina:
          saldainiai[i[1]] = [i[0], i[1], i[3]]

with open("pigiausi.txt", "w") as f:
    if saldainiai:
        for i in saldainiai.values():
            f.write(f"{i[0]} {i[1]} {i[2]}\n")
    else:
        f.write(f"Visi saldainiai brangesni nei {kaina}\n")

