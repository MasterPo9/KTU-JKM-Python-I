import math
import random
def random_math():
    nums=[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    num1=nums[int(random.uniform(0, 20))]
    num2=nums[int(random.uniform(0, 20))]
    op=["div", "mult", "sum", "min", "sqr"]
    operator=op[int(random.uniform(0, 5))]

    if operator=="div":
        print(num1/num2)
    elif operator=="mult":
        print(num1*num2)
    elif operator=="sum":
        print(num1+num2)
    elif operator=="min":
        print(num1-num2)
    elif operator=="sqr":
        print(num1**num2)
    print(f"-----DEBUG-----\nnum1={num1};num2={num2};operator={operator}") # Debug info for testing purposes
def kazkas():
    x=0
    while x==0:
        try:
            x=float(input("Amzius?: "))
        except Exception:
            print("Galima ivesti tik skaicius")
    day=x*365
    hour=day*24
    minute=hour*60
    second=minute*60
    print(f"Jusu amzius dienomis: {day}, valandomis: {hour}, minutemis: {minute}, sekundemis: {second}")
def text_mod():
    date=[]
    print("Laba diena!\nProgramuojame toliau!")
    print("Laba diena! \\n Programuojame toliau!\\n")
    print("Laba diena! \\n\nŠiandien sekmadienis!\\n\n")
    print("Laba diena! Koks tavo vardas?\nMano vardas Vardenis.\nLaba diena Vardenis!")
    print("Laba diena! Koks tavo vardas?\nMano vardas Vardenis.\nLaba diena Vardeni!\nKokia šiandien diena?\nSpalio 8")
    print("Laba diena!Kompiuteris klausia: \"Koks tavo vardas? \"\nVartotojas atsako: \"Mano vardas Vardenis.\“\nKompiuteris sveikina : \"Laba diena Vardeni.\"")
    print("pt2")
    list.append(date, int(input("Iveskite metus: ")))
    list.append(date, int(input("Iveskite menesi: ")))
    list.append(date, int(input("Iveskite diena: ")))
    print(f"\n (DEBUG) \n date={date}\n")
    print(f"Laba diena!\nĮveskite šios dienos datos metus\nĮveskite šios dienos datos mėnesį\nĮveskite šios dienos datos dieną\nŠiandien yra {date[0]} {date[1]} {date[2]}\nDatos skaičių suma = {date[0]+date[1]+date[2]}")
    print(f"Laba diena!")
    d=int(input("Įveskite šios dienos datos dieną:"))
    print(f"Nuo metų pradžios praėjo {31 + 28 + 31 + 30 + 31 +30 +31 + 31 + 30 + d} dienos")
    print(f"Laba diena!")
    m=int(input("Įveskite šios dienos datos mėnesį:"))
    d=int(input("Įveskite šios dienos datos dieną:"))
    print(f"Nuo metų pradžios praėjo ", (m-1) * 30 + 3 + d)
    print("*******************************\n* Labas. Mano vardas Vardenis.*\n*******************************")
    vardas=str(input("Mano vardas yra: "))
    print(f"*******************************\n* * * * * * * * * * *\n* Labas. Mano vardas {vardas}.*\n* * * * * * * * * * *\n*******************************")
def adv():
    sel=int(input("subselect: "))
    if sel==1:
        a=int(input("Kiek Andriui metų? "))
        print(f"Andriui yra {a} m.")
    if sel==2:
        # Laikrodis rodo x valandų ir y minučių. Parašykite programą, kuri apskaičiuotų, kiek
        #minučių m ir kiek sekundžių s prabėgo nuo vidurnakčio. Pasitikrinkite. Įvedę x = 3 ir y
        #= 5, turėtumėte gauti 185 minutes ir 11100 sekundžių.
        x=int(input("Kiek valandu?: "))
        y=int(input("Kiek minuciu?: "))
        m=x*60+y
        s=m*60
        print(f"Nuo vidurnakcio prabego {m} minuciu ir {s} sekundziu.")
    if sel==3:
        #Šiandien Tautvydas švenčia gimtadienį. Jam sukanka a metų. Parašykite programą, kuri
        #apskaičiuotų, kiek mėnesių (kintamasis - menesiu), dienų (kintamasis - dienu) ir
        #valandų (kintamasis - valandu) Tautvydas jau gyveno šiame pasaulyje. Tarkime, kad
        #metai turi 365 dienas. Pasitikrinkite. Įvedę 16 metų, turėtumėte
        #gauti 192 mėnesius, 5840 dienas ir 140160 valandas. Mėnesius, dienas ir valandas
        #išveskite atskirose eilutėse. Laikoma, kad kiekvienus metus sudaro lygiai 365 dienos.
        a=int(input("Kiek Tautvydui metu?: "))
        m=a*12
        d=a*365
        h=d*24
        print(f"Tautvydas gyveno {m} menesiu, {d} dienu ir {h} valandu.")
    if sel==4:
        a=int(input("Skaicius:"))
        x=(((a+5)*10)**2)/10
        x=int(x*10)/10
        print(x)
    if sel==5:
        print("cia reliai tsg as brute force padarysiu")
        rezultatas=5
        op=["div", "mult", "sum", "min", "sqr", "ediv", "liek"]
        while rezultatas != 125:
            rezultatas=5
            op1=op[int(random.uniform(0, 7))]
            op2=op[int(random.uniform(0, 7))]
            op3=op[int(random.uniform(0, 7))]
            if op1=="div":
                rezultatas/=2
            elif op1=="mult":
                rezultatas*=2
            elif op1=="sum":
                rezultatas+=2
            elif op1=="min":
                rezultatas-=2
            elif op1=="sqr":
                rezultatas**=2
            elif op1=="ediv":
                rezultatas//=2
            elif op1=="liek":
                rezultatas%=2
            if op2=="div":
                rezultatas/=5
            elif op2=="mult":
                rezultatas*=5
            elif op2=="sum":
                rezultatas+=5
            elif op2=="min":
                rezultatas-=5
            elif op2=="sqr":
                rezultatas**=5
            elif op2=="ediv":
                rezultatas//=5
            elif op2=="liek":
                rezultatas%=5
            if op3=="div":
                rezultatas/=3
            elif op3=="mult":
                rezultatas*=3
            elif op3=="sum":
                rezultatas+=3
            elif op3=="min":
                rezultatas-=3
            elif op3=="sqr":
                rezultatas**=3
            elif op3=="ediv":
                rezultatas//=3
            elif op3=="liek":
                rezultatas%=3
        print(f" rezultatas({op1})=2 rezulatas({op2})=5 rezultatas({op3})=3 = 125")



sel=int(input("select: "))
if sel==1:
    random_math()
if sel==2:
    kazkas()
if sel==3:
    text_mod()
if sel==4:
    adv()
