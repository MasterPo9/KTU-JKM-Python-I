import scrolltext as st

def vienas():
    it_paz=input("Klases IT savarankisko darbo pazymiai(kiekviena iskirkite tarpu arba kableliu): ")
    contains_sp=False
    contains_cm=False
    contains_both=False                                     #imput format precheck vars

    for i in range(0, len(it_paz)):
        if it_paz[i] == " ":
            contains_sp=True
        if it_paz[i] == ",":
            contains_cm=True                                #auto detect format (split by spaces, or commas)

    if contains_cm and contains_sp: 
        contains_both=True
        contains_cm, contains_sp=False, False               #or if both are used, split by both

    if contains_sp:
        it=it_paz.split(" ")

    if contains_cm:
        it=it_paz.split(",")

    if contains_both:
        it=it_paz.split(", ")                               #the actual split 

    maz=min(it)
    didz=max(it)    #why does ts not work
    didzc=0
    vid, k, sum=0, 0, 0

    for i in it:
        if i == "9" or i == "10":
            k+=1                                            #count how many instances of 9 or 10 appear in list
        sum+=int(i)
        if int(i) >= didzc:                                 #my own custrom max function
            didzc = int(i)
    vid=sum/len(it)                                         #average function
    print(f"min: {maz}\nmax: {didzc}\nvidurkis: {vid}\nmokiniu skaicius gavusiu 9 arba 10: {k}")
def n1():
    bgs=input("Kiekvieno draugo bagazo svoris: ")
    contains_sp=False
    contains_cm=False
    contains_both=False                                     #imput format precheck vars

    for i in range(0, len(bgs)):
        if bgs[i] == " ":
            contains_sp=True
        if bgs[i] == ",":
            contains_cm=True                                #auto detect format (split by spaces, or commas)

    if contains_cm and contains_sp: 
        contains_both=True
        contains_cm, contains_sp=False, False               #or if both are used, split by both

    if contains_sp:
        bg=bgs.split(" ")

    if contains_cm:
        bg=bgs.split(",")

    if contains_both:   
        bg=bgs.split(", ") 

    b=float(input("\nKiek euru tures moketi draugai uz 1 kg? "))

    kb=0
    didzc=0
    ct=1
    print(bg)
    for i in bg:
        kb+=float(i)
        if float(i) >= didzc:
            didzc=float(i)
            nr=ct
        ct+=1
    
    s=kb*b

    print(f"Visa mase: {kb}Kg\nMokestis: {s}Eur\nSunkiausiai nesancio keleivio numeris ir bagazo mase: {didzc}Kg, numeris {nr}")


def n2():
    prekes=st.cinput("Prekes kurias zmogus pirko: ")
    m=float(input("Kokia kaina uz kuria ne didesnes kainos? "))
    k, sum=0, 0

    for i in prekes:
        if float(i) <= m:
            k+=1
            sum+=float(i)
    print(f"Prekiu, kuriu kaina ne didesne kaip {m} Euru, yra k = {k}\nUz jas reikes moketi {sum} Euru")

def n3():
    ugiai=st.cinput("Merginu ugis zymimas sveikaisiais teigiamais, o vaikinu sveikaisiais neigiamais\nMokiniu ugiai centimetrais: ")
    summ, ctm, sumv, ctv=0, 0, 0, 0
    for i in ugiai:
        if int(i) < 0:
            sumv+=abs(int(i))
            ctv+=1
        elif int(i) > 0:
            summ+=int(i)
            ctm+=1
    vidvaikinu=sumv/ctv
    vidmerginu=summ/ctm
    print(f"vidvaikinu = {vidvaikinu}, vidmerginu {vidmerginu}")
def n4():
    taskai=st.cinput("Kiek kiekvienas daugiakovininkas surinko tasku? ")
    tmin=min(taskai)
    tmax=max(taskai)
    print(f"tmax = {tmax}, tmin = {tmin}")
n4()