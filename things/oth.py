import math
import sys
import time

import pkg.scrolltext as st


def sci_notation(x, acc=3):
    if x == 0:
        return "0"
    exp = int(math.log10(x))
    base = int(x / 10 ** (exp - acc))
    return f"{base}e{exp}"


def huge_int_summary(x, lead_digits=5, tail_digits=3):
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


sys.set_int_max_str_digits(999999)

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

print(f"Answer: {huge_int_summary(res)}")
