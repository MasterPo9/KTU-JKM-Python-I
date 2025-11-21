def main():
    M_questions = ["553234Maistas" ,"Kaip dažnai valgote mėsą?", "Ar maisto produktus perkate ūkininkų turgelyje, ekologiško maisto parduotuvėje?","Ar kompostuojate vaisių ir daržovių atliekas?","Ar pakuojate perkamus maisto produktus?","Kiek maisto išmetate per dieną?"]
    N_questions = ["3333Namai","Kur gyvenate?","Kiek kambarių jūsų namuose tenka žmogui?","Ar jūsų šeima turi antrą namą, pavyzdžiui sodybą, kuriame beveik nebūna?"]
    E_questions = ["3425Energija","Kokia oro temperatūra jūsų namuose šaltuoju metų laiku?", "Ar jūsų šaldytuvas naudoja mažai energijos?", "Kaip vėsinate namų ar automobilio orą?"]
    D_questions = ["74002044Daiktai", "Kiek vietos užima jūsų šios dienos šiukšlės?","Rūšiuojate popieriaus, metalo, stiklo, plastiko atliekas (-100 taškų).","Neišmetate daiktų, jei galima juos sutaisyti (-20 taškų).","Ar naudojate vienkartinius daiktus, jei galite rinktis daugkartinius?", "Naudojate įkraunamas baterijas, jei tai įmanoma (-30 taškų).","Kiek elektrinių prietaisų yra jūsų namuose?","Kaip dažnai naudojate buitinės technikos ir kitus elektrinius prietaisus?"]
    Dr_questions = ["70000244Drabužiai ir avalynė","Drabužius skalbiate po kiekvieno dėvėjimo (80 taškų).","Dėvite lopytus ar kitaip taisytus drabužius (-20 taškų).","Ketvirtadalį jūsų drabužių sudaro siūti rankomis arba dévéti drabužiai (-20 taškų)", "Kasmet atnaujinate didžiąją dalį garderobo (200 taškų).", "Ar atiduodate labdarai nebedėvimus drabužius?", "Kokią dalį turimų drabužių dėvite?","Kiek porų batų perkate per metus?"]
    T_questions = ["43443Transportas","Kaip kasdien pasiekiate mokyklą?","Kiek laiko per dieną jus veža automobiliu?","Kiek automobilių turi jūsų šeima?","Kiek kartų per metus skrendate lėktuvu?"]
    # x_questions[0]-->(lenght)-->ans_amount1, ans_amount2... 

    ans=["""· Daugiau nei 1 kartą per dieną (600 taškų)
    · 1 kartą per dieną (400 taškų)
    · 2 kartus per savaitę (300 taškų)
    · Esate vegetaras (200 taškų)
    · Esate veganas (150 taškų)""", 
    """· Ne (60 taškų)
    · Dalį maisto produktų (30 taškų)
    · Taip, visus maisto produktus (O taškų)""", 
    """· Ne (60 taškų)
    · Taip (-20 taškų)""", 
    """· Taip, visus (100 taškų)
    · Kai kuriuos (30 taškų)
    · Ne (O taškų)""", 
    """· Pusę nesuvartoto maisto (100 taškų)
    · Trečdalį nesuvartoto maisto (50 taškų)
    · Ketvirtadalį nesuvartoto maisto (25 taškai)
    · Neišmetate (O taškų)""",
    """· Nuosavame name už miesto (50 taškų)
    · Nuosavame name mieste (O taškų)
    · Bute (-50 taškų)""",
    """· Daugiau nei 3 kambariai (200 taškų)
    · 2-3 kambariai (100 taškų)
    · 1-2 kambariai (O taškų)""",
    """· Taip (400 taškų)
    · Taip, bet dalijatės su kita šeima, draugais (200 taškų)
    · Ne (O taškų)""",
    """· 22 C ir daugiau (150 taškų)
    · 19-22 ℃ (100 taškų)
    · 15-18 ℃ (50 taškų)
    · Mažiau nei 15 ℃ (-20 taškų)""",
    """· Ne (50 taškų)
    · Taip (-50 taškų)""",
    """· Oro kondicionieriumi namų orą (100 taškų)
    · Oro kondicionieriumi automobilio orą (50 taškų)
    · Ventiliatoriumi namų orą (-10 taškų)
    · Nevésinate (-50 taškų)""",
    """· Telpa į didelę šiukšliadėžę (200 taškų)
    · Telpa į nedidelę šiukšliadėžę (60 taškų)
    · Telpa į batų dėžę (20 taškų)
    · Neturite šiukšlių (-50 taškų)""",
    "","",
    """· Taip (60 taškų)
    · Ne (-50 taškų)""",
    "",
    """· Daugiau kaip 15 (200 taškų)
    · 10-15 (100 taškų)
    · 5-10 (75 taškai)
    · 0-5 (25 taškai)""",
    """· Dažnai (80 taškų)
    · Kartais (60 taškų)
    · Labai retai (20 taškų)
    · Nenaudojate (O taškų)""",
    "","","","",
    """· Ne (100 taškų)
    · Taip (-50 taškų)""",
    """· Mažiau kaip 25 proc. (100 taškų)
    · 50 proc. (75 taškai)
    · 75 proc. (50 taškų)
    · Daugiau nei 75 proc. (25 taškai)""",
    """· 7 poras ir daugiau (90 taškų)
    · 4-6 poras (60 taškų)
    · 2-3 poras (20 taškų)
    · Ne daugiau kaip 1 porą (O taškų)""",
    """· Automobiliu (100 taškų)
    · Viešuoju transportu (30 taškų)
    · Pésčiomis arba dviračiu (O taškų)""",
    """· Daugiau nei 60 min. (200 taškų)
    · 30-60 min. (100 taškų)
    · Mažiau nei 30 min. (40 taškų)
    · Neveža (O taškų)""",
    """· Daugiau nei 2 (200 taškų)
    · 2 (100 taškų)
    · 1 (50 taškų)
    · Neturi (20 taškų)""",
    """· Daugiau nei 2 kartus (400 taškų)
    · 1-2 kartus (200 taškų)
    · Neskrendate (O taškų)"""]

    points=[[600, 400, 300, 200, 150], [60, 30, 0], [60, -20], [100, 30, 0], [100, 50, 25, 0], [50, 0, -50], [200, 100, 0], [400, 200, 0], [150, 100, 50, -20], [50, -50], [100, 50, 0, -50], [200, 60, 20, -50], [-100], [-20], [60, -50], [-30], [200, 100, 75, 25], [80, 60, 20, 0], [80], [-20], [-20], [200], [100, -50], [100, 75, 50, 25], [90, 60, 20, 0], [100, 30, 0], [200, 100, 40, 0], [200, 100, 50, 20], [400, 200, 0]]

    print(len(ans))
    usr_ans=[]
    ct=1

    print("Parašykite atsakyma skaičiumi, kurį atsakyma renkatės.\n")

    lenghtm, lenghtn, lenghte, lenghtd, lenghtdr, lenghtt=int(M_questions[0][0]), int(N_questions[0][0]), int(E_questions[0][0]),int(D_questions[0][0]), int(Dr_questions[0][0]), int(T_questions[0][0])

    offsetm = lenghtm
    offsetn = lenghtn + offsetm
    offsete = lenghte + offsetn
    offsetd = lenghtd + offsete
    offsetdr = lenghtdr + offsetd
    offsett = lenghtt + offsetdr

    for i in range(1, len(ans)+1):
        if i<=offsetm and i==1: clenght, cq, off, ct=lenghtm, M_questions, offsetm, 1
        elif i<=offsetn and i==lenghtm+1: clenght, cq, off, ct= lenghtn, N_questions, offsetn, 1
        elif i<=offsete and i==offsetn+1: clenght, cq, off, ct= lenghte, E_questions, offsete, 1
        elif i<=offsetd and i==offsete+1: clenght, cq, off, ct= lenghtd, D_questions, offsetd, 1
        elif i<=offsetdr and i==offsetd+1: clenght, cq, off, ct= lenghtdr, Dr_questions, offsetdr, 1
        elif i<=offsett and i==offsetdr+1: clenght, cq, off, ct= lenghtt, T_questions, offsett, 1

        if ct==1:
            print(f"\n{cq[0][1+int(cq[0][0]):]}\n")
        
        if cq[0][ct] == "0" and ans[i-1] == "":
            print(f"\n{cq[ct]}\n1 Jeigu taip, 0 jeigu ne.")
        else:
            print(f"\n{cq[ct]}\n{ans[i-1]}")
        while True:
            try:
                x=(int(input()))
                if x not in range(0, len(points[i-1])+1):
                    raise(Exception)
                usr_ans.append(x)
                break
            except:
                print("Galima rasyti tik skaicius, kurie yra pasirenkami")



        ct+=1

    usr_points=[]
    ct=0

    for i in usr_ans:
        if i == 0:
            usr_points.append(0)
        else:
            try:
                usr_points.append(points[ct][i-1])
            except Exception as e:
                print(f"\nException: {e}\n\nCapped usr_points to a known acceptable value.\ndebug: i:{i}, ct:{ct}, usr_points:{usr_points}, usr_ans:{usr_ans}")
                try:
                    usr_points.append(points[ct][1])
                except Exception as f:
                    usr_points.append(50)
                    print(f"\nSecondary Exception: {f}.\n\nCapped usr_points to \"50\"")
        ct+=1

    sum=0

    for i in usr_points:
        sum+=int(i)

    print(f"\nJūs surinkote {sum} taškų")

try:
    main()
except Exception as e:
    print(f"Cought exception:\n {e}\n")