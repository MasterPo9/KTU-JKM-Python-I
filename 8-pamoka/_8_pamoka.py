import m9_utils as utils

# print(sum([int(x) for x in utils.listify(1234)]))
# print(f'\nyou will get {utils.gambling([f"{utils.LIGHT_WHITE}{utils.FAINT}zero{utils.RESET}", f"{utils.LIGHT_CYAN}one{utils.RESET}", f"{utils.CYAN}two{utils.RESET}", f"{utils.BLUE}three{utils.RESET}", f"{utils.LIGHT_GREEN}four{utils.RESET}", f"{utils.GREEN}five{utils.RESET}", f"{utils.LIGHT_PURPLE}six{utils.RESET}", f"{utils.PURPLEC}{utils.BOLD}seven{RESET}", f"{BLINK}{RED}{REDBG}{BOLD}{CURLYUNDERLINE}ten{RESET}"], [10, 5, 2.5, 1.25, 0.625, 0.3125, 0.15625, 0.078125, 0.0390625])} cents')

def v1():
    a = int(input("Iveskite skaiciu: "))
    s = utils.sum(a, 1)
    print(f"Skaitmenu suma: {s}")

def v2():
    a = int(input("Iveskite skaiciu: "))
    sand = 0
    while a>0:
        if sand == 0:
            sand = a%10
        else:
            sand *= a%10
        a //= 10
    print(f"Skaitmenu sandauga: {sand}")
def v3():
    a = int(input("Iveskite skaiciu: "))
    skaitmenu_kiekis = 0
    while a>0:
        skaitmenu_kiekis += 1
        a //= 10
    print(f"Skaitmenu kiekis: {skaitmenu_kiekis}")
def v4():
    a = int(input("Iveskite skaiciu: "))
    lyg, nelyg = 0, 0
    while a>0:
        if a%10%2==0:
            lyg += 1
        else:
            nelyg += 1
        a //= 10
    print(f"Nelyginiu: {nelyg}\nLyginiu: {lyg}")

def v5():
    a = int(input("Iveskite skaiciu: "))
    t = 0
    while a>0:
        t = a%10
        a //= 10
    print(f"Pirmasis skaitmuo: {t}")

def v6():
    a = int(input("Iveskite skaiciu(a): "))
    b = int(input("Iveskite skaiciu(b): "))
    t1 = 0
    t2 = 0
    while a>0:
        t1 = a%10
        a //= 10
    while b>0:
        t2 = b%10
        b //= 10
    sum = t1+t2
    print(f"Pirmuju Skaitmenu suma: {sum}")

def v7():
    n = int(input("Iveskite skaiciu: "))
    sum = 0
    cn = 1
    out = ""
    while sum != n:
        sum += cn
        if sum == n:
            out = "TAIP"
        if cn == n:
            out = "NE"
            break
        cn += 1
    print(out)

def v8():
    n = int(input("Iveskite skaiciu: "))
    cn = 1
    dal = []
    while cn <= n:
        if n/cn==float(n//cn):
            dal.append(cn)
        cn += 1
    if dal == [1, n]:
        print(f"{n} yra pirminis")
    else:
        print(f"{n} yra sudetinis")

def v9():
    a = int(input("Iveskite skaiciu(a): "))
    b = int(input("Iveskite skaiciu(b): "))
    dal1, dal2 = [], []
    cn = 1
    while cn <= a:
        if a/cn==float(a//cn):
            dal1.append(cn)
        cn += 1

    cn = 1
    while cn <= b:
        if b/cn==float(b//cn):
            dal2.append(cn)
        cn += 1

    bendr_dal = []
    for i in dal1:
        if i in dal2:
            bendr_dal.append(i)
    if bendr_dal == [1]:
        print(f"Duotieji Skaiciai yra tarpusavije pirminiai ({bendr_dal})")
    else:
        print(f"Duotieji Skaiciai nera tarpusavije pirminiai ({bendr_dal})")

def v10():
    a = int(input("Iveskite skaiciu: "))
    power = 0
    raised = 0
    while raised <= a:
        power += 1
        raised = 2 ** power
    print(2**(power-1))

def v11():
    a = int(input("Koks nuotolis? "))
    b = int(input("Kiek daugiau iveikdavo? "))
    c = int(input("Kiek nusliuostas nuotolis turi virsyti? "))
    t = 0
    s = 0
    while a<c:
        a += b
        t += 1
        s += a
    print(f"{t}")

def v12():
    m = int(input("Kiek saldainiu jis rado? "))
    d = 1
    while m>0:
        m -= d
        d += 1
    print(d-1)

def v13():
    sek = utils.cinput("Iveskite seka: ", True, True, DEBUG=True)
    vid = sum(sek)/len(sek)
    print(vid)

