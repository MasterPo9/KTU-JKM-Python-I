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


def cinput(a="Input: ", INTMODE=False):
    it = []
    it_paz = input(f"{a}")

    digits_rlenght = []
    digits_nl_lenght = 0
    digits_rletter = ""

    MODE = None
    list_of_all_letters.remove(chr(32))

    for i in it_paz:
        if i in numbers:
            INTMODE = True
            MODE = "NUM"
            digits_nl_lenght += 1
            digits_rletter += str(i)
        elif i in list_of_all_letters:
            INTMODE = False
            MODE = "LTR"
            if i == ".":
                MODE = "NUM"
                digits_nl_lenght += 1
                digits_rletter += str(i)
                INTMODE = True
            digits_nl_lenght += 1
            digits_rletter += str(i)
        else:
            MODE = "SEP"
            digits_nl_lenght = 1
            digits_rlenght.append(digits_rletter)
            digits_rletter = ""

    if digits_rletter:  # append the last buffer
        digits_rlenght.append(digits_rletter)

    if INTMODE:  # try converting to int first, then float
        it_int = []
        for i in digits_rlenght:
            try:
                it_int.append(int(i))
            except:
                it_int.append(float(i))
        return it_int
    else:
        return digits_rlenght


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
