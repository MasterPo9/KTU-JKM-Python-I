import scrolltext as st


def ka():
    def dal(sk):
        sum = 0
        for i in str(sk):
            sum += int(i)
        return sum

    aq = int(input("iveskite skaiciu "))
    w = dal(aq)
    print(w)


#mane uzkniso klausyt
def uzd1():
    znks_k = int(input("Iveskite zinksniu kieki iki mokyklos: "))
    sprg, supj = 0, 0
    for i in range(1, znks_k + 1):
        if i % 10 == 0:
            supj += 1
        elif i % 10 == 5:
            sprg += 1
    print(f"Suplojimu bus {supj}, spragtejimu - {sprg}")


def uzd2():
    tmp = st.cinput("Iveskite, kiek snaigiu nukrito per pirmaja sekunde ir kiek sekundziu snigo: ", True)
    k, n = int(tmp[0]), int(tmp[1])  # n - kiek sekundziu snigo; k - kiek snaigiu iskrito pirma sekunde
    s = 0
    for i in range(1, n + 1):
        s += k
        k *= 2
    print(s)


def uzd3():
    st_d = int(input("Parasykite kuria savaites diena prasidejo menuo: "))
    intervalas = st.cinput("Iveskite dienu intervala: ", )
    pr, end = intervalas[0], intervalas[1]  # get first day and last day of interval
    prd = pr // 7  # calculate int(floor) week count
    sav_d = prd * 7  # this should then be the day, closest to pr, having the same week day as "st_d" (the entered week day)
    skr = pr - sav_d  # the difference between the start of the interval and "sav_d" (the day, closest to the start of the interval, having the same week day as the entered week day)
    sav_d_pr = st_d + skr - 1  # calculation of the week day, for the start of the interval
    if sav_d_pr > 7:
        sav_d_pr -= 7  # line 45 can overflow above 7(there are only 7 week days), so it must "start" a new week
    for i in range(pr, end + 1):
        print(f"{i}-oji diena: {sav_d_pr}")
        sav_d_pr += 1
        if sav_d_pr > 7:  # overflow check
            sav_d_pr = 1


def uzd3a():
    st_d = int(input("Parasykite kuria savaites diena prasidejo menuo: "))
    msdl = []
    for i in range(1, 31 + 1):  #generate list of all week days in a month
        msdl.append(st_d)
        st_d += 1
        if st_d > 7:
            st_d = 1
    intervalas = st.cinput("Iveskite dienu intervala: ", )
    pr, end = (intervalas[0]), (intervalas[1])
    for i in range(pr, end + 1):
        print(f"{i}-oji diena: {msdl[i - 1]}")


def uzd4():
    kl = st.cinput("Iveskite kiek isrideno tasku , ant kiekvieno kauliuko: ", True)
    max = len(kl) * 6
    surinko = sum(kl)
    vid = surinko / len(kl)
    if surinko <= max // 2:
        laimejo = "Loterija pralaimeta"
    else:
        laimejo = "Loterija laimeta"
    print(f"Is viso buvo galima surinkti tasku: {max}\nTomas is viso surinko {surinko} tasku\nJo tasku vidurkis: {vid} Tasko\n{laimejo}")


def uzd5():
    prk = st.cinput("Iveskite pirkiniu kainas: ", True)
    svr = st.cinput("Iveskite pirkiniu svorius: ", True)
    vid = sum(prk) / len(prk)
    e = vid // 100
    ct = vid - e * 100
    ssvr = sum(svr)
    print(f"Pirkinio vidutine kaina: {e:.0f} eurai {ct:.0f} ct.")
    st.printif(ssvr > 5000, "Petriukas negales parnesti pirkiniu.")
    st.printif(ssvr <= 5000, "Petriukas gales parnesti pirkinius.")


uzd5()
