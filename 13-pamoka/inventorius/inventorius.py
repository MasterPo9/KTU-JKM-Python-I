global inventorius

def remove_item():
    global inventorius
    daiktas = input("Įveskite daikto pavadinimą, kurį norite pašalinti. ")
    if daiktas not in inventorius:
        print("Tokio daikto inventoriuje nėra!")
    elif daiktas in inventorius:
        inventorius.remove(daiktas)
        write_items()
        print(f"{daiktas} buvo pašalintas iš inventoriaus.")
    rescan()

def add_item():
    global inventorius
    daiktas = input("Įveskite daikto pavadinimą, kurį norite pridėti. ")
    if daiktas in inventorius:
        print("Toks daiktas inventoriuje jau yra!")
    elif not daiktas:
        print("Daikto pavadinimas negali būti tuščias!")
    elif len(inventorius)>7:
        print("Daiktas negali būti pridėtas, dėl pasiekto limito (8)!")
    else:
        inventorius.append(daiktas)
        write_items()
        print(f"{daiktas} buvo pridėtas į inventorių.")
    rescan()

def main():
    global inventorius
    rescan()
    while True:
        print(f"Jūs savo inventoriuje turite ({len(inventorius)}/8):")
        for i in inventorius: print(i)
        pasirinkimas = input("Paspauskite \"r\" jeigu norite pašalinti daiktą iš inventoriaus, o \"a\" jeigu norite pridėti naują daiktą. ")
        if pasirinkimas.lower() == "r":
            remove_item()
        elif pasirinkimas.lower() == "a":
            add_item()
        else:
            print("Tokio pasirinkimo nėra!")


def write_items():
    global inventorius
    with open("inventorius.txt", "w") as f:
        f.writelines(str(i)+"\n" for i in inventorius)

def rescan():
    global inventorius
    with open("inventorius.txt", "r") as f:
        inventorius = [i.strip() for i in f.readlines()]

main()