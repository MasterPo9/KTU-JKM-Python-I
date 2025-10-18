"""
Užduotis: Matematika

Petriukas per pusmetį gavo 5 matematikos pažymius. Mokytoja nusprendė padaryti vaikams
staigmeną: mokiniai, kurių pažymių vidurkis yra didesnis už 9, gaus tris saldainius, o mokiniams,
kurių vidurkis yra tarp 7 ir 9, įskaitant intervalo galus, bus apdovanoti dviem saldainiais. Visi
likusieji gaus po vieną saldainį. 

Parašykite programą, kuri pagal įvestus Petriuko pažymius apskaičiuotų, kiek saldainių jis gaus. 

Duomenys                                                Rezultatai
Kokius pažymius gavo Petriukas? 8 9 6 5 10              Petriukas gaus du saldainius
Kokius pažymius gavo Petriukas? 10 10 8 9 10            Petriukas gaus tris saldainius
Kokius pažymius gavo Petriukas? 5 5 4 5 5               Petriukas gaus vieną saldainį 
"""

# Rašyk savo kodą žemiau 👇

pazymiai = input("Kokius pažymius gavo Petriukas? ")
pazymiai_list = pazymiai.split()
pazymiai_int = [int(x) for x in pazymiai_list]
vidurkis = sum(pazymiai_int) / len(pazymiai_int)
if vidurkis > 9:
    print("Petriukas gaus tris saldainius")
elif vidurkis >= 7 and vidurkis <= 9:
    print("Petriukas gaus du saldainius")
else:
    print("Petriukas gaus vieną saldainį")
