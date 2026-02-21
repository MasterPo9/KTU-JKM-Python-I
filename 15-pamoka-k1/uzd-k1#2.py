with open("knygos.txt", "r") as f:
    knygos = [i.strip().split(";") for i in f.readlines()]

autorius = input("Įveskite autorių, pagal kurį norėtumėte surasti knygas. ")
rastu_knygu_kiekis = 0
for i in knygos:
    pavadinimas, autorius_l, metai, kaina = i
    if autorius_l == autorius:
        rastu_knygu_kiekis += 1
        print(f"{pavadinimas}: {metai}, {kaina}")
if rastu_knygu_kiekis == 0:
    print("Tokio autoriaus knygų biblioteka neturi")

brangesne_kaina: float = float(input("Įveskite kainą, kuria būtų surastos knygos kurios yra brangesnės arba tokios pačios kainos įvestai. "))
brangesnes = []


for i in knygos:
    pavadinimas, autorius_l, metai, kaina = i
    if float(kaina) >= brangesne_kaina:
        brangesnes.append(f"{pavadinimas};{autorius_l};{kaina}\n")

with open("brangesnes.txt", "w") as f:
    f.writelines(brangesnes)


unikalus_autoriai = []

for i in knygos:
    pavadinimas, autorius_l, metai, kaina = i
    if autorius_l not in unikalus_autoriai:
        if not unikalus_autoriai:
            print(f"Unikalūs autoriai:")

        print(autorius_l)
        unikalus_autoriai.append(autorius_l)

