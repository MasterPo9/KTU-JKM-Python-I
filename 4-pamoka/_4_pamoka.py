import scrolltext as st
import random
def v1():
    skaiciai = st.random_num_list(5, 1, 5)
    vaisiai = ["obuolys", "bananas", "kriause", "slyva", "vynuoge"]
    availible_vars = []
    for i in range(0, len(skaiciai)+1):
        exec(f"n{i}='{vaisiai[skaiciai[i-1]-1]}'")
        availible_vars.append(f"n{i}")
    print(availible_vars)
    for i in range(len(availible_vars)+1):
        exec(f"print(f\"Kintamasis {availible_vars[i]} yra lygus {{ {availible_vars[i]} }}\")")
def v2():
    skaiciai = [1, 1, 1, 1 ,1, 1]
    n=0
    for i in skaiciai:
        if i == 1:
            n+=1
    print(f"rasta {n} vienetu")
def v3():
    sk = [2,5,8,7,9,5,1,5]
    n=0
    for i in sk:
        if i == 5:
            n+=1
    print(f"rasta {n} penketu")
    if 2 in sk:
        print("True")
def v4():
    n=[5,3,2,4,10]
    suma=0
    for i in n:
        suma+=i

exe=input("")
exec(f"{exe}")