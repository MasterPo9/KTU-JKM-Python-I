"""
LEGACY - PLEASE DON'T USE (use only for some unknown functions)
"""

list_of_all_letters = [chr(i) for i in range(32, 33)] + [chr(46)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in
                                                                                                       range(97, 123)]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


def scroll(text, color='0F', speed=0.001, SINGLE_LINE_MODE=False):
    import time
    import os
    os.system(f'color {color}')

    x = ""
    start = time.time()
    for i in range(0, len(text)):
        for a in range(0, len(list_of_all_letters)):
            if SINGLE_LINE_MODE:
                print(f"\r{x + list_of_all_letters[a]}", end="")
            else:
                print(x + list_of_all_letters[a])
            if text[i] == list_of_all_letters[a]:
                break
            time.sleep(speed)
        x += text[i]
        if text == x:
            break
    print(x)


def tetr(x, n=2, r=2):
    # basicly tetration function, Tetration is repeated exponentiation.
    # n -- the power, r -- the number of times to repeat exponentiation
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        for i in range(r):
            x **= n


def printif(expr, msg=""):
    if expr:
        print(msg)


def input_list(prompt="", separator=","):
    return input(prompt).split(separator)


def random_text(length=10):
    import random
    text = ""
    for i in range(length):
        text += list_of_all_letters[int(random.uniform(0, len(list_of_all_letters)))]
    return text


def random_color():
    import random
    hex_chars = "0123456789ABCDEF"
    color = ""
    for i in range(2):
        color += hex_chars[int(random.uniform(0, len(hex_chars)))]
    return color


def random_num_list(length=5, min_val=0, max_val=100):
    import random
    num_list = []
    for i in range(length):
        num_list.append(int(random.uniform(min_val, max_val)))
    return num_list


def cinput(a="Input: ", Force_Number_Input=False, Float_Force_Extension=False, Preferred_Value_Amount=0,
           Force_Preferred_Value_Amount=False, DEBUG=False, LTSEFC="", BOLTS=False, RFoBOLTL=0, PEI3o1="",
           PMP=0.1):  # if Preferred Value Amount is 0, then it will essentially be disabled.
    if Float_Force_Extension and not Force_Number_Input:
        Float_Force_Extension = False

    if Preferred_Value_Amount == 0 and Force_Preferred_Value_Amount:
        Force_Preferred_Value_Amount = False

    if RFoBOLTL != 1 or RFoBOLTL != 3:
        PEI3o1 = ""

    list_of_all_letters__type_ns = list_of_all_letters
    try:
        list_of_all_letters__type_ns.remove(chr(32))
    except:
        pass

    MODE = MODE1 = MODE2 = ""

    FLOATMODE = False
    INTMODE = False

    INTMODE_PERM_FALSE = False
    if DEBUG: print("Debug Enabled!")

    while True:

        it_paz = input(f"{a}")

        digits_collected = []
        digits_nl_lenght = 0
        digits_rletter = ""

        MODE = None

        for i in it_paz:
            if i in numbers:
                INTMODE = True
                MODE2 = MODE1
                MODE1 = MODE
                MODE = "NUM"
                digits_nl_lenght += 1
                digits_rletter += str(i)
                if DEBUG: print(f"\r\x1b[K{digits_rletter};{MODE}←{MODE1}←{MODE2}; {digits_nl_lenght}")
            elif i in list_of_all_letters__type_ns:
                if Force_Number_Input and not Float_Force_Extension: continue
                INTMODE = False
                MODE2 = MODE1
                MODE1 = MODE
                MODE = "LTR"
                if i == "." and MODE1 == "NUM":
                    MODE2 = MODE1
                    MODE1 = MODE
                    MODE = "NUM"
                    digits_nl_lenght += 1
                    digits_rletter += str(i)
                    INTMODE = True
                    FLOATMODE = True
                    if Force_Number_Input and Float_Force_Extension: continue
                elif (MODE1 == "SEP" or MODE2 == "SEP") and i == ".":
                    MODE = "SEP"
                    continue
                else:
                    if Force_Number_Input and Float_Force_Extension: continue
                    INTMODE_PERM_FALSE = True
                    if DEBUG: print("Enabled Permanent INTMODE")
                if Force_Number_Input and Float_Force_Extension: continue
                digits_nl_lenght += 1
                digits_rletter += str(i)
                if DEBUG: print(f"\r\x1b[K{digits_rletter};{MODE}←{MODE1}←{MODE2}; {digits_nl_lenght}")
            else:
                if MODE != "SEP":
                    digits_nl_lenght = 1
                    digits_collected.append(digits_rletter)
                    if DEBUG: print(
                        f"Appended before changing of MODE(prev {MODE}←{MODE1}←{MODE2}) to SEP({digits_rletter})")

                MODE2 = MODE1
                MODE1 = MODE
                MODE = "SEP"

                digits_rletter = ""
                if DEBUG: print(f"\r\x1b[K{digits_rletter};{MODE}←{MODE1}←{MODE2}; {digits_nl_lenght}")

        if digits_rletter:
            digits_collected.append(digits_rletter)
        if DEBUG: print(f"Gotten result: {digits_collected}")

        if Force_Preferred_Value_Amount and len(digits_collected) != Preferred_Value_Amount:
            if RFoBOLTL == 1 or RFoBOLTL == 3:
                if PEI3o1:
                    print(PEI3o1)
                else:
                    print(f"List Doesnt Match required length ({Preferred_Value_Amount})!")
            if RFoBOLTL == 0:
                print(f"List Doesnt Match required length ({Preferred_Value_Amount})!")
            continue

        if (len(digits_collected) > Preferred_Value_Amount * (1 + PMP) or len(
                digits_collected) < Preferred_Value_Amount * (
                    1 - PMP)) and Preferred_Value_Amount != 0 and not Force_Preferred_Value_Amount:
            if len(digits_collected) > Preferred_Value_Amount * (1 + PMP):
                if RFoBOLTL == 1 or RFoBOLTL == 3 or RFoBOLTL == 0:
                    if PEI3o1 and RFoBOLTL != 0:
                        print(PEI3o1)
                    elif RFoBOLTL == 0:
                        print("List is too long!")
                    if RFoBOLTL == 2 or RFoBOLTL == 3:
                        continue

            if len(digits_collected) < Preferred_Value_Amount * (1 - PMP):
                if LTSEFC:
                    print(LTSEFC)
                else:
                    print("List is too short!")
                if BOLTS:
                    continue
        break

    rem_empt_res = []
    ct = 0
    cte = 0
    ctne = 0
    for i in digits_collected:
        ct += 1
        if i == "":
            cte += 1
            if DEBUG: print(f"Found empty value in list (#l-{ct}/#e-{cte})")
            continue
        else:
            rem_empt_res.append(i)
            ctne += 1
            if DEBUG: print(f"Found not empty value in list (#l-{ct}/#ne-{ctne})")
    if not INTMODE_PERM_FALSE:
        it_int = []
        for i in digits_collected:
            if INTMODE and not FLOATMODE:
                it_int.append(int(i))
            elif INTMODE and FLOATMODE:
                it_int.append(float(i))
        return it_int
    else:
        return digits_collected


def lmax(a=None):
    if a is None:
        a = []
    kb = 0
    didzc = 0
    ct = 1
    for i in a:
        kb += float(i)
        if float(i) >= didzc:
            didzc = float(i)
        ct += 1
    return didzc
# :3

def sci_notation(x, acc):
    exp = len(str(x)) - 1
    base = int(str(x)[acc])
    return f"{base}e{exp}"
