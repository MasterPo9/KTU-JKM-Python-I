# failas = open("failas.txt", mode="rt")
# text=failas.read()
# print(text)
# failas.close()

# with open("failas.txt", encoding="utf-8") as f:
#     text = [i.strip() for i in f.read().splitlines()]
#     print(text)
#     f.readlines()
#     f.seek(0)

import m9_utils as utils

def v1():
    with open("vaisiai.txt") as f:
        for line in f:
            pavadinimas, kaina=line.strip().split(";")
            print(f"{utils.generate_gradient(text=f'{pavadinimas} kainuoja {kaina}', output=False)}")

def v2():
    sum=0
    with open("uzdarbis.txt") as f:
        for line in f:
            sum+=float(line.strip())
    print(sum)

def v3():
    sum=0
    liniju_kiekis=0
    with open("pazymiai.txt") as f:
        for line in f:
            sum+=float(line.strip())
            liniju_kiekis+=1
        vid=sum/liniju_kiekis
    print(round(vid,1))

def v4():
    with open("skaiciai.txt") as f:
        text = [int(i.strip()) for i in f.read().splitlines()]
        didz = max(text)
    print(f"Didžiausias faile esantis skaičius: {didz}")

def v5():
    sum=0
    liniju_kiekis=0
    neigiama, teigiama = 0, 0
    with open("orai.txt") as f:
        for line in f:
            linijos_suma = float(line.strip())
            sum+=linijos_suma
            liniju_kiekis+=1
            if linijos_suma < 0: neigiama+=1
            else: teigiama += 1

    vid=sum/liniju_kiekis
    print(f"Vidutinė oro temperatūra: {round(vid,1)}")
    if teigiama > neigiama: print("Daugiau buvo teigiamų dienų.")
    elif neigiama > teigiama: print("Daugiau buvo neigiamų dienų.")
    else: print("Dienų buvo vienodai")

def v6():
    sum=0
    with open("cekis.txt") as f:
        text = [i.strip() for i in f.read().splitlines()]
        for i in text:
            preke, kaina, kiekis = i.split(";")
            sum+=float(kiekis)*float(kaina)

    print(f"Bendra apsipirkimo suma yra {sum} Eur.")

def namas():
    sum, suml, sumr = 0, 0, 0
    ctl, ctr = 0, 0
    with open("namai.txt") as f:
        text = [i.strip() for i in f.read().splitlines()]
        for line in text:
            numeris, gyventojai=line.split(" ")
            sum += int(gyventojai)
            if int(numeris) % 2 == 0:
                sumr += int(gyventojai)
                ctr += 1
            else:
                suml += int(gyventojai)
                ctl += 1
    vidl=suml/ctl
    vidr=sumr/ctr
    formatted = f"{sum}\n{suml}\n{sumr}\n{vidl}\n{vidr}"

    print(formatted)
    file=open("rezultatas.txt","w")
    file.write(formatted)
    file.close()

def grybas():
    grybu_duomenis = []
    data_menesis = []
    data_diena = []
    mase = []
    baravykai = []
    raudonvirsiai = []
    with open("grybai.txt") as f:
        text = [i.strip() for i in f.read().splitlines()]
        for i in text:
            grybu_duomenis.append(i.split(" "))
    for a in grybu_duomenis:
        data_menesis.append(a[0])
        data_diena.append(a[1])
        mase.append(a[2])
        baravykai.append(a[3])
        raudonvirsiai.append(a[4])


    derl_date_index = mase.index(max(mase))
    derl_data = f"{data_menesis[derl_date_index]} {data_diena[derl_date_index]}"
    bara_date_index = baravykai.index(max(baravykai))
    baravykai_derl_data = f"{data_menesis[bara_date_index]} {data_diena[bara_date_index]}"
    raud_date_index = raudonvirsiai.index(max(raudonvirsiai))
    raudonvirsiai_derl_data = f"{data_menesis[raud_date_index]} {data_diena[raud_date_index]}"

    print(f"Derlingiausia baravykų diena: {baravykai_derl_data}")
    print(f"Derlingiausia raudonviršių diena: {raudonvirsiai_derl_data}")
    utils.rainbow(f"Derlingiausia diena: {derl_data}")

def ledai():
    suma = 0
    with open("ledai.txt") as f:
        k, m, n = [int(y) for y in [i.strip() for i in f.read().splitlines()][0].split(" ")]

    for i in range(n):
        suma += k
        k += m
    print(suma)

def sultys():
    with open("sultys.txt") as f:
        tekstas = [int(i.strip()) for i in f.read().splitlines()]
    for i in tekstas:
        penkiu_litru_talpa, dvieju_litru_talpa, vieno_litro_talpa=0, 0, 0
        while i >= 5:
            penkiu_litru_talpa += 1
            i -= 5
        if i % 5 > 0:
            while i % 2 == 0 and i > 0:
                dvieju_litru_talpa += 1
                i -= 2
            if i == 1 or i%2==1:
                vieno_litro_talpa += 1
                i-=1
        print(penkiu_litru_talpa, dvieju_litru_talpa, vieno_litro_talpa)

sultys()