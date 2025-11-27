"""
A simple scrolling text animation in the console.
Imports: time, os
Function: scroll(text, color='0F', speed=0.001)
may contain other useful functions"""

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
                print(f"\r\x1b[K{x + list_of_all_letters[a]}")
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


def cinput(a="Input: ", Force_Number_Input=False, Float_Force_Extension=False, LEGACY=False, DEBUG=False):
    if Float_Force_Extension and not Force_Number_Input:
        Float_Force_Extension = False

    MODE = MODE1 = MODE2 = ""

    FLOATMODE = False
    INTMODE = False

    INTMODE_PERM_FALSE = False
    if DEBUG: print("Debug Enabled!")

    it_paz = input(f"{a}")

    digits_collected = []
    digits_nl_lenght = 0
    digits_rletter = ""

    MODE = None
    list_of_all_letters.remove(chr(32))

    for i in it_paz:
        if i in numbers:
            INTMODE = True
            MODE2 = MODE1
            MODE1 = MODE
            MODE = "NUM"
            digits_nl_lenght += 1
            digits_rletter += str(i)
            if DEBUG: print(f"\r\x1b[K{digits_rletter};{MODE}←{MODE1}←{MODE2}; {digits_nl_lenght}")
        elif i in list_of_all_letters:
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

    if not INTMODE_PERM_FALSE:  # try converting to int first, then float
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


def sci_notation(x, acc):
    exp = len(str(x)) - 1
    base = int(str(x)[acc])
    return f"{base}e{exp}"
