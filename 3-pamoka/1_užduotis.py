"""
Duoti du skaičiai a ir b. Sukurkite funkciją, kuri nustatytų, ar šių skaičių suma yra lygi 5.
"""

# Rašyk savo kodą žemiau 👇
a=float(input("Iveskite pirma skaiciu: "))
b=float(input("Iveskite antra skaiciu: ")) 
if a + b == 5:
    print("Suma lygi 5")
else:
    print(f"Suma nelygi 5 (bet ji lygi {a+b})")
