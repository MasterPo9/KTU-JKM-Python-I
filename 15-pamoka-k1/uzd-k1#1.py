pradzia = int(input("Įveskite sekos pradžią "))
pabaiga = int(input("Įveskite sekos pabaigą "))
zingsnis = int(input("Įveskite sekos žingsnį "))


kiekis = 0
for i in range(pradzia, pabaiga, zingsnis):
    if i % 5 == 0 and i > 20:
        print(i)
        kiekis += 1

if kiekis:
    print(f"Rasta: {kiekis}")
else:
    print("Nieko nerasta")
