import scrolltext as st
import random
def v1():
    sk=st.random_num_list(int(random.uniform(7, 12)), -10, 10)
    print(sk)
    t, n=0, 0
    for i in sk:
        if i<0: n+=1
        if i>0: t+=1
    print(f"teigiamu: {t}, neigiamu: {n}")
def v2():
    # Architektas suprojektavo salę, kurioje bus n eilių. Pirmoje eilėje
    # stovės k kėdžių, o kiekvienoje kitoje eilėje – 2 kėdėmis daugiau, negu
    # prieš tai buvusioje. Parašykite programą, kuri apskaičiuotų, kiek iš viso
    # kėdžių (s) reikia užsakyti, kad architekto sumanymas būtų
    # įgyvendintas. Pasitikrinkite kai n = 3, o k = 8, turi būti spausdinama: s =
    # 30 kėdžių.
    n=int(input("Eiliu skaicius: "))
    k=int(input("Pirmos eiles kedziu skaicius: "))
    s=0
    for i in range(1, n+1):
        s+=k+2*(i-1)
    print(f"Kedziu skaicius: {s}")
def v3():
    # Parašykite programą funkcijos y=x
    # ^4+2x^3+3x^2+2x+1 reikšmei
    # paskaičiuoti. Pasitikrinkite kai x=-5; -1; 3; 6.
    x=int(input("x = "))
    y=x**4+2*x**3+3*x**2+2*x+1
    print(y)
def v4():
    # Vaikui gimus tėvas padovanojo 5 litus. Kiekvienais kitais metais
    # gimtadienio proga padovanodavo tiek litų, kiek jam sueidavo metų.
    # Parašykite programą, kuri suskaičiuotų, kiek jis turės litų, kai jam
    # sueis n metų. Pasitikrinkite. Kai n = 16, tai s =141.
    n=int(input("Kiek metu? "))
    s=0
    if n > 0: s+=5
    for i in range(1, n+1):
        s+=i
    print(f"Jis tures {s} Eur")
#                                       --------------------SKIP------------------------
def v6():
    s=0
    for i in range(1, 101):
        s+=i
    print(f"s = {s}")
def v7():
    n=int(input("dydis: "))
    s=0
    for i in range(1, n+1):
        s+=i
    print(f"s = {s}")
def v8():
    m=int(input("dydis1: "))
    n=int(input("dydis2: "))
    s=0
    sk=list(range(m, n+1))
    for i in sk:
        s+=i
    print(f"s = {s}")
def v9():
    m=int(input("dydis1: "))
    n=int(input("dydis2: "))
    s=0
    sk=list(range(m, n+1))
    for i in sk:
        s+=i**2
    print(f"s = {s}")
def v10():
    n=int(input("skaicius: "))
    dal=[]
    for i in range(1, n+1):
        if n%i==0:
            list.append(dal, i)
    print(dal)
def v11():
    n=int(input("skaicius: "))
    dal=[]
    for i in range(1, n+1):
        if n%i==0:
            list.append(dal, i)
    s=0
    m=1
    for i in dal:
        s+=i
        m*=i
    print(f"Dalikliai: {dal}, Ju yra {len(dal)}. Ju suma yra {s}, o sandauga {m}")
def v12():
    n=int(input("Skaicius: "))
    dal=[]
    
    for i in range(1, n+1):
        if n%i==0:
            list.append(dal, i)
    if len(dal)==2:
        t="yra pirminis"
    elif len(dal)>2:
        t="yra sudetinis"
    else:
        t="nezinau kas yra"
    print(f"{n} {t}")
def v13():
    sek=input("Iveskite seka, iskirdami skaicius tarpais: ")
    sk=sek.split(" ")
    s, st, mn=0, 0, 1
    t, n= [], []
    for i in sk:
        s+=int(i)
        if int(i)<0: list.append(n, int(i))
        if int(i)>0: list.append(t, int(i))
    for i in t:
        st+=int(i)
    for i in n:
        mn*=int(i)
    s2=s**2
    v=s/len(sk) 
    print(f"sumos kvadratas yra {s2}, aritmetinis vidurkis yra {v:.1f}, teigiamų narių suma yra {st}, o neigiamų narių sandauga yra {mn}.")
def v14():
    t=int(input("pradinio stebejimo temperatura: "))
    temp_p=input("temperaturos pokyciai, iskirdami tarpu: ")
    temp=temp_p.split(" ")
    for i in temp:
        t+=int(i)
    print(f"Galutine temperatura yra {t} laipsniai")
def v15():
    while True:
        n=int(input("Skaicius didesnis uz 2:"))
        if not n>2:
            print("Blogai ivestas skaicius, bandykite dar karta")
        else:
            break
    a1=1
    a2=-2
    for i in range(3, n+1):
        s=a1+a2
        a1=a2
        a2=s
    print(f"a{n}={a2}")
def v16():
    n=int(input("Uogienes sauksteliu skaicius: "))
    
    M=2
    K=5
    F=3
    ct=0
    skip=False
    apss=input("Apsilankymai, iskiriami tarpu: ")
    aps=apss.split(" ")
    for i in aps:
        if int(i) == 1:n-=M
        if skip:
            skip=False 
            print(f"Skipped M! (cycle {ct+1}, {nn})")
            n=nn
        if n<5: 
            skip=True
            nn=n
        else: 
            nn=n
            print(f"Didnt skip! (cycle {ct+1}K, {nn})")
        if int(i) == 2: n-=K
        if skip:
            skip=False 
            print(f"Skipped K! (cycle {ct+1}, {nn})")
            n=nn
        if n<3: 
            skip=True
            nn=n
        else: 
            nn=n
            print(f"Didnt skip! (cycle {ct+1}F, {nn})")
        if int(i) == 3: n-=F
        if skip:
            skip=False 
            print(f"Skipped F! (cycle {ct+1}, {nn})")
            n=nn
        if n<2: 
            skip=True
            nn=n
        else: 
            nn=n
            print(f"Didnt skip! (cycle {ct+1}M, {nn})")
        ct+=1
    
    print(n, "(graceful)")
    for ct, i in enumerate(aps, start=1):
        if i == '1':
            n -= M
            print(f"Applied M (cycle {ct}, {n})")
        elif i == '2':
            n -= K
            print(f"Applied K (cycle {ct}, {n})")
        elif i == '3':
            n -= F
            print(f"Applied F (cycle {ct}, {n})")
        if n <= 0:
            n = 0
            break
    print(n, "(ungraceful)")
v16()