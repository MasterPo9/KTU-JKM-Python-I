import math
import sys
import time
from threading import Thread

import gmpy2

import m9_utils as utils
import m9_utils.scrolltext as st

stopped = False
disabled = False

def sometimer(x=str(), type=1):
    global stopped
    if type == 1:
        nahh = time.time()
        while not stopped:
            print(f"\r{time.time() - nahh:.2f}s ({x})", end="")
            time.sleep(0.01)
    if type == 2:
        nahh = time.time()
        ct = 0
        additional_dots = ""
        while not stopped:
            print(f"\r{x} ({time.time() - nahh:2.2f}s){additional_dots}", end="")
            time.sleep(0.1)
            if ct % 10:
                additional_dots += "."
                once = False
            else:
                once = True


def sci_notation(x, acc=3):
    if x == 0:
        return "0"
    exp = int(math.log10(x))
    base = int(x / 10 ** (exp - acc))
    return f"{base}e{exp}"


def huge_int_summary(x, lead_digits=5, tail_digits=3):  # ts wont work ig
    start3 = time.time()
    try:
        start3 = time.time()
        if x == 0:
            return "0"
        print(f"{time.time() - start3}s")
        num_digits = int(math.log10(x)) + 1
        print(f"{time.time() - start3}s")
        lead = x // 10 ** (num_digits - lead_digits)
        print(f"{time.time() - start3}s")
        tail = x % 10 ** tail_digits
        print(f"{time.time() - start3}s")
        return f"{lead}...(x{num_digits - lead_digits - tail_digits})...{tail}"
    except:
        print(f"{time.time() - start3}s")
        quit()


def WOO_LETS_MAKE_THIS_WORK(x=int(), status=False,
                            status_type=0):  # and ofc the x is the massive number calculated down below
    # so you know how this number itself is very big?
    # well it isn`t that big by its int length ig..
    # but we need to set it to str first

    global stopped

    eval_start = time.time()

    digits = math.floor(2 ** times * math.log10(num)) + 1
    if status and status_type == 0:
        stopped = False
        p = Thread(target=sometimer(f"Converting \033[1mres\033[0m({digits} digits) to gmpy2 mpz type", 2), daemon=True)
        p.start()

    gx = gmpy2.mpz(x)

    if status and status_type == 0:
        stopped = True
        time.sleep(1)
        stopped = False

        p = Thread(target=sometimer(f"Converting \033[1mres\033[0m({digits} digits) to str", 2), daemon=True)
        p.start()

    xstr = str(gx)

    if status and status_type == 0:
        stopped = True
        time.sleep(1)
        stopped = False

        p = Thread(target=sometimer("Formatting answer", 2), daemon=True)
        p.start()

    xsum = f"{xstr[:4]}...(x{len(xstr) - 8})...{xstr[-4:]}"

    stopped = True

    utils.generate_gradient(text=f"ANSWER: {xsum}\nTook {time.time() - eval_start:.2f}s to evaluate.")


sys.set_int_max_str_digits(99999999)

conv_l = st.cinput(
    "Input 3 numbers(1st -- the number to raise; 2nd -- the power to raise by; 3rd -- the times to raise): ", True)
num = conv_l[0]
power = conv_l[1]
times = conv_l[2]
res = num
once = "Do That!"
err_ct = 0
max_err_ct = 5

for i in range(0, times):
    try:
        start = time.time()
        prev = res
        res *= res
        end = time.time()
        took = end - start
        print(f"time for iter #{i}: {took:.6f}.")
        if took > 1 and not disabled:
            question = input(f"Do you want to continue? The times will exponentially increase from here. The next iteration is expected to take {(took*2):.0f}s. [y/n] ")
            if question == "n":
                exit(0)
            disabled = True
        if once == "Do That!":
            start2 = time.time()
            print(
                f"Value is {sci_notation(res // num * 100, 3)}% bigger than starting value ({sci_notation(res // prev * 100, 3)}% bigger than previous value).")
            end2 = time.time()
            if once == "Do That!":
                print(f"Full took time: {(end2 - start2 + took):.2f}s")
            took2 = end2 - start2
            if took2 > 1 and once == "Do That!":
                once = "Do not do that anymore 3:"
                print(f"Print function calculation time >1s. Stopping secondary feedback.")
    except OverflowError:
        err_ct += 1
        if err_ct >= max_err_ct:
            raise "Maximum number of errors reached."
        continue

WOO_LETS_MAKE_THIS_WORK(res)
