
import math
def goofy_oneliner():
    print(f"Plytelių kaina: {int(input("Įveskite kambario ilgį: ")) * int(input("Įveskite kambario plotį: "))* int(input("Įveskite m2 plytelių kainą: ")) *1.05} Eur") #lol oneliner
def main_jkm():
    subsel=int(input("Galimi pasirinkimai:\n1. Konsekto kopijavimas\n2. Laikrodis\n3. Taudvydas\n4. Knygos bibliotekos lankytojui\n5. Keleiviai traukinyje\n6. Stačiakampio plotas ir perimetras\n7. Tarakonas\n8. Kazkoks isprotejes verslininkas moka bauda tonomis\nPasirinkite: "))
    if subsel ==1:
        # 1. Parašykite programą, kuri apskaičiuotų, kiek popieriaus lapų k reikės norint nukopijuoti konspektą visos
        # klasės mokiniams. Žinoma, kad klasėje yra n mokinių ir konspektą sudaro m lapų.
        # Pasitikrinkite. Įvedę n = 20 ir m = 10, turėtumėte gauti k = 200.
        n = int(input("Įveskite mokinių skaičių klasėje: "))
        m = int(input("Įveskite konspekto lapų skaičių: "))
        k = n * m
        print(f"Popieriaus lapų skaičius: {k}")
    elif subsel==2:
        # 2. Laikrodis rodo x valandų ir y minučių. Parašykite programą, kuri apskaičiuotų, kiek minučių m ir kiek
        # sekundžių s prabėgo nuo vidurnakčio.
        # Pasitikrinkite. Įvedę x = 3 ir y = 5, turėtumėte gauti: m = 185, s = 11100.
        x = int(input("Įveskite valandas: "))
        y = int(input("Įveskite minutes: "))
        m = x * 60 + y
        s = m * 60
        print(f"Nuo vidurnakčio prabėgo {m} minučių ir {s} sekundžių")
    elif subsel==3:
        a=int(input("Kiek metu sukanka taudvydui? "))
        men=a*12
        d=a*365
        v=d*24
        print(f"Taudvydas gyvena {men} menesiu, {d} dienu ir {v} valandu.")
    elif subsel==4:
    
        # 4. Parašykite programą, kuri apskaičiuotų, kiek knygų k vidutiniškai per metus perskaito vienas mokyklos
        # bibliotekos lankytojas. Žinomas vidutiniškai per vieną mėnesį perskaitytų knygų skaičius v ir vidutiniškai
        # per metus apsilankiusiųjų bibliotekoje skaičius n.
        # tikrinkite. Įvedę v = 120, n = 800, turėtumėte gauti k = 2.
        v=int(input("Vidutiniskas per menesi perskaitytu knygu skaicius: "))
        n=int(input("Vidutiniskas per metus apsilankiusiuju bibliotekoje skaicius: "))
        k=v*12/n # per metus perskaitytu knygu lankytojo skaicius
        print(f"Per metus perskaitytu knygu lankytojo vidutiniskas skaicius: {k}")
    elif subsel==5:
        # Rašyk savo kodą žemiau 👇
        # 5. Parašykite programą, kuri apskaičiuotų, kiek vidutiniškai keleivių k važiuoja į Vìlnių viename traukinio
        # vagone, jei žinomas traukinio keleivių skaičius n, keleivių, vykstančių ne į Vìlnių, skaičius m ir vagonų
        # skaičius v.
        # Pasitikrinkite. Įvedę n = 100, m = 20 ir v = 4, turėtumėte gauti k = 20.

        n=int(input("Traukinio keleiviu skaicius: "))
        m=int(input("Keleiviu vykstanciu ne i vilniu skaicius: "))
        v=int(input("Traukinio vagonu skaicius: "))
        #keleiviu vieno vagono, keliaujanciu i vilniu skaicius
        k=(n-m)/v
        print(f"Keleiviu vieno vagono, keliaujanciu i vilniu skaicius: {k}")
    elif subsel==6:
        #6. Parašykite programą, kuri apskaičiuotų stačiakampio, kurio viršutinio kairiojo taško (x1; yl) ir apatinio
        # dešiniojo taško (x2; y2) koordinatės yra sveikieji skaičiai, plotą s ir perimetrą p. Nurodytų taškų koordinatės
        # įvedamos klaviatūra. Stačiakampio kraštinės lygiagrečios su koordinačių ašimis.
        # Pasitikrinkite. Kai x1 = 0, yl =5, x2=4, y2 = 0, turi būti spausdinama:
        # Stačiakampio plotas s = 20 kvadr. vnt.
        # Stačiakampio perimetras p = 18 vnt.

        x1 = int(input("Įveskite stačiakampio viršutinio kairiojo taško x1 koordinatę: "))
        y1 = int(input("Įveskite stačiakampio viršutinio kairiojo taško y1 koordinatę: "))
        x2 = int(input("Įveskite stačiakampio apatinio dešiniojo taško x2 koordinatę: "))
        y2 = int(input("Įveskite stačiakampio apatinio dešiniojo taško y2 koordinatę: "))
        a=abs(x1+x2) #stačiakampio kraštinė
        b=abs(y1+y2) #stačiakampio kraštinė
        s=a*b #stačiakampio plotas
        p=2*(a+b) #stačiakampio perimetras
        print(f"Stačiakampio plotas s = {s} kvadr. vnt.")
        print(f"Stačiakampio perimetras p = {p} vnt.")
    elif subsel==7:
        # 7. Tarakonas yra vienas greičiausių gyvūnų. Jo greitis yra g kilometrų per valandą. Apskaičiuokite, kiek centi-
        # metrų c tarakonas nubėga per sekundę.
        # Pasitikrinkite. Kai g = 1.08, turi būti spausdinama:
        # c= 30 cm
        g=float(input("Įveskite tarakono greitį (km/h): "))
        c=g*10**5/3600 #tarakono greitis cm/s
        print(f"c= {c} cm/s")
    elif subsel==8:
        # 8. Vienas garsus Lietuvos pramogų pasaulio atstovas per kito garsaus pramogų atstovo vestuves klaidingai
        # informavo policiją apie užminuotą pokylio vietą. Teismas paskyrė sumokėti k tūkstančių litų baudą. Kal-
        # tininkas baudą sumokėjo 1 cento monetomis. Kiek kilogramų m monetų buvo nuvežta į banką, jei viena
        # 1 cento moneta sveria 0,83 gramo?
        # Pasitikrinkite. Kai k = 15000, turi būti spausdinama:
        # m = 1245 kg
        k=int(input("Įveskite baudą (tūkstančiais litų): "))
        m=k*(10**5)*0.83/10**6
        print(f"m = {m} kg")
def papild():
    subsel=int(input("Galimi pasirinkimai:\n1. Savaites nuo metu pradzios\n2. Oliampiada\n3. Balionai\n4. Saldainiai\n5. Cukrus\n6. Vanduo\n7. Zvejys\nPasirinkite: "))
    if subsel==1:
        # Rašyk savo kodą žemiau 👇
        # 1. Parašykite programą, kuri apskaičiuotų, kiek pilnų savaičių w yra praėję nuo metų pradžios, jei žinomas
        # dienų skaičius d nuo metų pradžios.
        # Pasitikrinkite. Įvedę d = 15, turėtumėte gauti w = 2.
        d=int(input("Dienos nuo metų pradžios: "))
        w=d//7 #savaitės
        print(f"Savaitės: {w}")
    elif subsel==2:
        #Miesto informatikos olimpiadoje dalyvavo devintokai. Mokytoja nupirko saldainių „Nomeda“ ir išdalijo mokiniams
        # po lygiai. Saldainių neliko arba liko mažiau, negu yra mokinių. Po kiek saldainių gavo kiekvienas mokinys ir kiek
        # saldainių liko mokytojai?
        # Pavyzdžiai
        # Įvestis:
        # 7 (pirmas skaičius - devintokų kiekis)
        # 23 (antras skaičius - saldainių kiekis)
        # Išvestis:
        # 3 (po kiek sadainių gavo mokinys)
        # 2 (kiek mokytojai liko saldainių)
        n=int(input("Įveskite devintokų kiekį: "))
        m=int(input("Įveskite saldainių kiekį: "))
        k=m//n #po kiek saldainių gavo mokinys
        l=m%n #kiek mokytojai liko saldainių
        print(f"Po kiek sadainių gavo mokinys: {k}")
        print(f"Kiek mokytojai liko saldainių: {l}")
    elif subsel==3:
        #Andrius septintojo gimtadienio proga gavo balionų. Su draugais nusprendė balionus paleisti į dangų. Dalis
        # pučiamų balionų sprogo. Likusius balionus Andrius pasidalijo su draugais po lygiai. Jeigu po dalybų dar liko
        # balionų, tai juos pasiėmė Andrius. Po kiek balionų gavo kiekvienas draugas ir kiek balionų teko Andriui?
        # Parašykite programą šiam uždaviniui spręsti.
        # Pasitikrinkite. Jei balionų buvo 77, draugų buvo 7, 3 balionai sprogo, tai kiekvienas draugas gavo po 9 balionus,
        # o Andriui teko 11 balionų.
        # Pavyzdžiai
        # Įvestis:
        # Kiek Andrius gavo balionų?
        # 77
        # Kiek buvo draugų?
        # 7
        # Kiek balionų sprogo?
        # 3
        # Išvestis:
        # Draugai gavo po: 9
        # Andriui teko: 11
        b=int(input("Kiek Andrius gavo balionų? "))
        d=int(input("Kiek buvo draugų? "))
        s=int(input("Kiek balionų sprogo? "))
        l=b-s #likę balionai
        k=l//(d+1) #po kiek balionų gavo kiekvienas draugas
        a=int(l%(d+1)+k) #kiek balionų teko Andriui
        print(f"Draugai gavo po: {k}")
        print(f"Andriui teko: {a}")
    if subsel==4:
        # Saulius labai mėgsta saldainius. Mama kiekvieną dieną jam nuperka po n saldainių, tačiau leidžia suvalgyti tik m
        # saldainių, o likusius paslepia. Praėjus k dienų mamos slėptuvėje Saulius surado saldainius ir nusprendė
        # apskaičiuoti, kelioms dienoms tų saldainių užteks, jei valgys po m saldainių. Jei paskutinei dienai saldainių liktų
        # mažiau, tai pavaišins draugus - kiekvienam po vieną saldainį. Kiek draugų pavaišins Saulius?
        # Pasitikrinkite: jei n = 5, m = 2, k = 3, kompiuterio ekrane turi būti rodomi rezultatai: dienų: 4, draugų: 1.
        # Pavyzdžiai
        # Įvestis:
        # Kiek mama nuperka saldainių?
        # 5
        # Kiek mama leidžia suvalgyti?
        # 2
        # Po kiek dienų Saulius surado saldainius?
        # 3
        # Išvestis:
        # dienų: 4
        # draugų: 1
        n=int(input("Kiek mama nuperka saldainių? "))
        m=int(input("Kiek mama leidžia suvalgyti? "))
        k=int(input("Po kiek dienų Saulius surado saldainius? "))
        l=n-m #saldainiai paslepti per diena
        s=l*k #saldainiai paslepti per k dienas
        d=s//m #dienos kiek uzteks saldainiu
        a=s%m #saldainiai liks paskutinei dienai
        if a>0:
            draugai=a #kiek draugų pavaišins Saulius
        else:
            draugai=0
        print(f"dienų: {d}")
        print(f"draugų: {draugai}")
    elif subsel==5:
        # Cukraus kilogramo kaina yra m eurų (realusis skaičius). Maiše telpa k kilogramų cukraus (sveikasis skaičius).
        # Šeima perka n maišų cukraus visiems metams.
        # Parašykite programą, kuri apskaičiuotų, kokią pinigų sumą suma sumokės šeima už perkamą cukrų.
        # Pasitikrinkite: kai m = 0.85, k = 50, n = 2, tai suma yra 85.00.
        # Pavyzdžiai
        # Įvestis:
        # Kokia kilogramo kaina? 0.85
        # Kiek maiše telpa cukraus (kg)? 50
        # Kiek šeima perka maišų? 2
        # Išvestis:
        # 85.00
        m=float(input("Kokia kilogramo kaina? "))
        k=int(input("Kiek maiše telpa cukraus (kg)? "))
        n=int(input("Kiek šeima perka maišų? "))
        suma=m*k*n #suma kurią šeima sumokės už perkamą cukrų
        print(f"Kainuos {suma} Eur")
    elif subsel==6:
        #Vandens saugykloje yra v kubinių metrų vandens (realusis skaičius). Saugyklos vandenį vartoja n žmonių.
        # Vienas žmogus per parą vidutiniškai sunaudoja tam tikrą kiekį kubinių metrų vandens (realusis skaičius).
        # Parašykite programą, kuri apskaičiuotų, kelioms paroms užteks saugykloje esančio vandens. Atsakymą
        # suapvalinkite iki 2 skaičių po kablelio.
        # Pasitikrinkite: kai v = 1001, n = 50, vidutinis sunaudojimas yra 0.1, tai parų kiekis yra 200.2.
        # Pavyzdžiai
        # Įvestis:
        # Kiek saugykloje yra vandens? 1001
        # Kiek žmonių vartoja vandenį? 50
        # Kiek vienas žmogus suvartoja vandens? 0.1
        # Išvestis:
        # 200.20
        v=float(input("Kiek saugykloje yra vandens? "))
        n=int(input("Kiek žmonių vartoja vandenį? "))
        s=float(input("Kiek vienas žmogus suvartoja vandens? "))
        p=v/(n*s) #parų kiekis užteks saugykloje esančio vandens
        print(f"Užteks {p} parų")
    elif subsel==7:
        #Žvejys pagavo k vidutinio dydžio karosų, kurių vienas sveria e kilogramų, m vidutinio dydžio ešerių, kurių vienas
        # sveria n kilogramų ir x aukšlių, kurių viena sveria y kilogramų.
        # Parašykite programą, skaičiuojančią, kiek kilogramų žuvies iš viso pagavo žvejys. Atsakyme išveskite du
        # skaitmenis po kablelio.
        # Pasitikrinkite: kai k = 5, e = 1.5, m = 7, n = 0.45, x = 12, y = 0.09, tuomet žvejys iš viso pagavo 11.73 kg. žuvies.
        # Pavyzdžiai
        # Įvestis:
        # Kiek karosų pagavo žvejas? 5
        # Kiek vidutiniškai sveria vienas karosas? 1.5
        # Kiek ešerių pagavo žvejas? 7
        # Kiek vidutiniškai sveria vienas ešerys? 0.45
        # Kiek aukšlių pagavo žvejas? 12
        # Kiek vidutiniškai sveria viena aukšlė? 0.09
        # Išvestis:
        # 11.73
        k=int(input("Kiek karosų pagavo žvejas? "))
        e=float(input("Kiek vidutiniškai sveria vienas karosas? "))
        m=int(input("Kiek ešerių pagavo žvejas? "))
        n=float(input("Kiek vidutiniškai sveria vienas ešerys? "))
        x=int(input("Kiek aukšlių pagavo žvejas? "))
        y=float(input("Kiek vidutiniškai sveria viena aukšlė? "))
        s=k*e+m*n+x*y
        print(f"Žvejys iš viso pagavo {s} kg. žuvies.")
    elif subsel==8:
        # Parašykite programą, skaičiuojančią, kelias knygas vidutiniškai perskaito vienas skaitytojas, jei iš viso n
        # skaitytojų perskaitė k knygų. Rezultatą pateikite trijų ženklų po kablelio tikslumu.
        # Pasitikrinkite: kai n = 7, k = 50, tuomet atsakymas - 7.143.
        # Pavyzdžiai
        # Įvestis:
        # Kiek žmonių skaitė knygas? 7
        # Kiek jie perskaitė knygų? 50
        # Išvestis:
        # 7.143
        n=int(input("Kiek žmonių skaitė knygas? "))
        k=int(input("Kiek jie perskaitė knygų? "))
        s=k/n
        print(f"Vidutiniškai perskaito vienas skaitytojas: {s:.3f}")
    elif subsel==9:
        # Parašykite programą, skaičiuojančią žinomo spindulio r (realusis skaičius) apskritimo ilgį c. n reikšmę aprašykite
        # kaip konstantą. Laikykite, kad n = 3.141592. Rezultatą išveskite dviejų skaitmenų po kablelio tikslumu.
        # Pasitikrinkite: kai r = 2.5, tuomet c = 15.71.
        # Pavyzdžiai
        # Įvestis:
        # Koks spindulys? 2.5
        # Išvestis:
        # 15.71
        r=float(input("Koks spindulys? "))
        n=3.141592
        c=2*n*r #apskritimo ilgis
        print(f"Apskritimo ilgis: {c:.2f}")
    elif subsel==10:
        #Parašykite programą, skaičiuojančią, koks yra Ričardo pažymių vidurkis, jei vaikinas per pusmetį gavo 5
        # pažymius. Apskaičiuotą vidurkį išveskite 2 ženklų po kablelio tikslumu.
        # Pasitikrinkite: kai pažymiai yra 7, 5, 10, 8, 6, tuomet vidurkis yra 7.20.
        # Pavyzdžiai
        # Įvestis:
        # 7

        # 5

        # 10

        # 8

        # 6
        # Išvestis:
        # 7.20
        a=int(input("Iveskite pirma pazymi: "))
        b=int(input("Iveskite antra pazymi: "))
        c=int(input("Iveskite trecia pazymi: "))
        d=int(input("Iveskite ketvirta pazymi: "))
        e=int(input("Iveskite penkta pazymi: "))
        v=(a+b+c+d+e)/5 #vidurkis
        print(f"Vidurkis: {v:.2f}")
    elif subsel==11:
        #Klaviatūra įvedami keturi skaičiai, kurie reiškia atkarpos, nubrėžtos koordinačių plokštumoje, galų taškų A (x1;
        # y1) ir B (x2; y2) koordinates. Parašykite programą, skaičiuojančią atkarpos AB ilgį. Atsakyme palikite 2 skaičius
        # po kablelio.
        # Norėdami išspręsti šį uždavinį susiraskite kaip apskaičiuoti atstumą tarp dviejų taškų.
        # Pasitikrinkite: kai x1 = 0, y1 = 0, x2 = 0, y2 = 5, turi būti spausdinama: Atkarpos AB ilgis yra lygus 5.00 vnt.
        # Pavyzdžiai
        # Įvestis:
        # Įveskite x1: 0
        # Įveskite y1: 0
        # Įveskite x2: 0
        # Įveskite y2: 5
        # Išvestis:
        # 5.00
        x1 = int(input("Įveskite x1: "))
        y1 = int(input("Įveskite y1: "))
        x2 = int(input("Įveskite x2: "))
        y2 = int(input("Įveskite y2: "))
        AB=math.sqrt((x2-x1)**2+(y2-y1)**2) #atkarpos AB ilgis
        print(f"Atkarpos AB ilgis yra lygus {AB} vnt.")


sel=int(input("Galimi pasirinkimai:\n1. Goofy oneliner\n2. 2 pamoka JKM\n3. Papildomi\nPasirinkite: "))
if sel==1:
    goofy_oneliner()
elif sel==2:
    main_jkm()
elif sel==3:
    papild()
