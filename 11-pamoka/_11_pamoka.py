# eilute=10
# eilute*=2
# for i in range(1, int(eilute/2+1)):
#     print(f"{' '*(eilute//2-i)}{'#'*i}{' '*(eilute//2-i)}")

def v1():
    eilute=int(input("Iveskite eilutes ilgi: "))
    for i in range(1, eilute+1):
        for j in range(i):
            print("*", end="")
        print()

def v2():
    skait=int(input("Iveskite skaiciu: "))
    skaiciai=[]
    skaiciai.extend(str(skait))
    for i in skaiciai:
        for j in range(int(i)):
            print(i, end="")

def v3():
    n=int(input("Įveskite intervalo pradžią n: "))
    m=int(input("Įveskite intervalo pabaigą m: "))
    sksum = 0
    for i in range(n, m+1):
        for j in str(i):
            sksum+=int(j)
        print(f"Skaciaus {i} skaitmenu suma: {sksum}")
        sksum = 0

def v4():
    skait=int(input("Iveskite skaiciu: "))
    kvadrato_suma=0

    for i in range(1, skait+1):
        for j in range(1, i+1):
            kvadrato_suma+=j**2
        print(i, kvadrato_suma)
        kvadrato_suma = 0

def v5():
    skait=int(input("Iveskite skaiciu: "))
    for i in range(1, skait+1):
        for j in range(i):
            print(i,end="")
        print()

def v6():
    kv_did=int(input("Iveskite kvadrato dydi: "))
    ct = 1
    for y in range(1, kv_did+1):
        for x in range(kv_did):
            print(ct, end=" ")
            ct+=1
        print()

def v7():
    aukstis=int(input("Iveskite auksti: "))

    for i in range(1, aukstis+1):
        for j in range(i):
            print(i, end="")
        print()
    for i in range(aukstis-1, 0, -1):
        for j in range(i):
            print(i, end="")
        print()

ex=str(input("enter func: "))
exec(ex)
