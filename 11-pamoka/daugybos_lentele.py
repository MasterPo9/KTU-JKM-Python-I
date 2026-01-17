print("   ", end="")
pat1="---"
pat2="+"
sep=""
for y in range(1, 11):
    ly=len(str(y))
    if y != 1:
        print(f"{' ' if ly < 3 else ''}{y}{' ' if ly < 2 else ''}", end='')
    else:
        for i in range(1, 11):
            sand = i * y
            lxy = len(str(sand))
            formated = f"|{' ' if lxy < 3 else ''}{sand}{' ' if lxy < 2 else ''}"
            print(formated, end="")
        print()
        for a in range(1, 12):
            if a == 11:
                sep += pat1
            else:
                sep += pat1 + pat2
        print(sep)
        sep = ""
        print(f"{' ' if ly < 3 else ''}{y}{' ' if ly < 2 else ''}", end='')
    for x in range(1, 11):
        sand=x*y
        lxy=len(str(sand))
        formated=f"|{' ' if lxy < 3 else ''}{sand}{' ' if lxy < 2 else ''}"
        print(formated, end="")
    print()
    if y != 10:
        for a in range(1, 12):
            if a == 11:
                sep+=pat1
            else:
                sep+=pat1+pat2
        print(sep)
        sep=""