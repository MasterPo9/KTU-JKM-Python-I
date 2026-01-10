"""
Užduotis: Bankas

Sąlyga:

1. Bankas turi leisti vartotojui pasitikrinti balansą arba išeiti iš banko.

2. Bankas turi leisti vartotojui įnešti ir išimti pinigus į/iš sąskaitos.

3. Bankas turi turėti PIN kodą:
    - Vartotojas turi įvesti PIN kodą prieš įeinant į banką.
    - Jei PIN neteisingas, spausdinti „Neteisingas PIN“ ir užbaigti programą.

4. BONUS 1: Programa turi leisti vartotojui keisti PIN kodą.

5. BONUS 2: Programa turi saugoti veiksmų istoriją ir leisti peržiūrėti paskutinius 3 veiksmus.

6. BONUS 3: Programa turi skaičiuoti palūkanas arba premijas sąskaitai:
    - Kiekvieną kartą, kai vartotojas baigia operacijas, bankas prideda 1% nuo esamo balanso kaip premiją.

********************************************************
!!!!!   PASTABA: BONUS užduotys nėra privalomos    !!!!!
********************************************************
"""

import hashlib
import os

# Savo kodą rašyk žemiau:

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')
def pause():
    os.system('pause' if os.name == 'nt' else '')

def code_check(ch, for_check=False, fc_input_prompt=""):

    if not for_check:
        var = input('Įveskite PIN koda: ').encode('utf-8')
    else:
        var = input(fc_input_prompt).encode('utf-8')
    hashed_var = hashlib.md5(var).hexdigest()
    if hashed_var == ch:
        clr()
        if not for_check:
            print("Jus įvedėte teisingą koda.")
            pass
        else:
            return 300
    else:
        clr()
        if not for_check:
            exit("403: Forbidden")
        else:
            return 403

def check_history(history=3):
    hist_long=log(get_list=True)
    hist=hist_long[len(hist_long)-history:]
    print(f"Paskutinių trejų veiksmų istorija(Skaičiai pagal veiksmo naujuma):\n3. {hist[0]}\n2. {hist[1]}\n1. {hist[2]}")
    log("Peržiūrėta veiksmų istorija.")

action_history = []
def log(action :str="", get_list :bool= False):
    if not get_list:
        action_history.append(action)
    else:
        return action_history

def change_pass(old_code :str):
    returned_status_code=code_check(old_code, True, "Iveskite savo seną PIN kodą. ")
    if returned_status_code == 403:
        clr()
        print("Neteisingas PIN kodas.")
        log("Bandyta pakeisti PIN kodą, bet įvestas neteisingas senas PIN kodas.")
    if returned_status_code == 300:
        clr()
        var = input("Įveskite naują PIN kodą: ").encode('utf-8')
        hashed_var = hashlib.md5(var).hexdigest()
        var = ""
        code=hashed_var
        print("PIN kodas pakeistas sėkmingai.")
        log("PIN kodas buvo pakeistas.")
        return code
    return old_code


balansas = 100.0
code = "ee389847678a3a9d1ce9e4ca69200d06"



def check_balance(bal):
    clr()
    print(f"Jus turite {bal} EUR savo balanse.\n")
    log(f"Pažiūrėta kiek pinigų balanse ({bal}EUR).")
    pause()

def take_money(bal):
    clr()
    isimti=abs(float(input("Kiek EUR išimti iš balanso? ")))
    if bal >= isimti:
        bal -= isimti
        print(f"Sėkmingai išimti {isimti} EUR iš balanso.")
        log(f"Išimta {isimti}EUR iš balanso.")
    else:
        print(f"Jūs neturite užtenkamai pinigų balanse, kad galėtumėte išimti {isimti} EUR ({isimti}>{bal})")
        log(f"Nepavyko iš balanso išimti {isimti}EUR dėl pinigų trūkumo.")

    return bal

def add_money(bal):
    clr()
    ideti=abs(float(input(f"Kiek EUR įnešti į balansą? ")))
    bal+=ideti
    print(f"Sėkmingai įnešta {ideti} EUR į balansa.")
    log(f"Įnešta {ideti}EUR į balansa.")
    return bal

def main(balansas):
    global code
    while True:
        try:
            code_check(code)

            while True:
                print("\nPasirinkite veiksmą:")
                print("1 - Patikrinti balansą.")
                print("2 - Išimti pingus iš balanso.")
                print("3 - Įnešti pingus į balansą.")
                print("4 - Peržiūrėti veiksmų istoriją.")
                print("5 - Pakeisti PIN kodą.")

                print("\n6 - Atsijungti.")

                pasirinkimas=input("\nĮveskite savo pasirinkimą. ")

                if pasirinkimas=="1":
                    check_balance(balansas)
                if pasirinkimas=="2":
                    balansas=take_money(balansas)
                if pasirinkimas=="3":
                    balansas=add_money(balansas)
                if pasirinkimas=="4":
                    check_history()
                if pasirinkimas=="5":
                    code=change_pass(code)
                if pasirinkimas=="6":
                    clr()
                    log(f"Atsijungta iš banko. (pridėta {balansas*0.01:.2f}EUR kaip premija)")
                    print(f"Sėkmingai atsijungta ir pridėta {balansas*0.01:.2f}EUR kaip premija. ")
                    balansas*=1.01

                    break
        except Exception as e:
            print(f"ERROR: {e}\n{pause()}\n")

main(balansas)



