import scrolltext as st
def p1():
    x=st.cinput("Iveskite skaicius: ", True)
    s=sum(x)
    vid=s/len(x)
def p2():
    zd=str.lower(str(input("Iveskite zodi: ")))
    prb=[]
    b=[]
    b.extend("aeyuioąęėįųū")
    prb.extend("qzwsxdcrfvgtbhnjmklpčšž")
    bsk=0
    prbsk=0
    for i in zd:
        if i in b:
            bsk+=1
        if i in prb:
            prbsk+=1
    print(f"Balsiu: {bsk}\nPriebalsiu: {prbsk}")

def p3():
    sk=float(input("Iveskite skaiciu: "))
    sum=sk
    laips=int(input("Iveskite laipsni: "))
    for i in range(1, laips):
        sum*=sk
    print(sum)

def p4():
    n=int(input("Suma iki "))
    x=list(range(1, n+1))
    s=sum(x)
    print(f"Suma: {s}")

def p5():
    riba=int(input("Riba: "))
    sk=st.cinput("Skaiciai: ", True)
    big=[]
    for i in sk:
        if i>riba:
            big.append(i)
    
    print(f"Didesni uz riba: {big}")

def p6():
    sk=st.cinput("Iveskite skaicius: ", True)
    for i in sk:
        if sk.count(i)>1:
            for x in range(1, sk.count(i)+1):
                sk.remove(i)
    print(f"Unikalus skaiciai: {sk}")

def p7():
    zodis=str(input("Iveskite zodi: "))