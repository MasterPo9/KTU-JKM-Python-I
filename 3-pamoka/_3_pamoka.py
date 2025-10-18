import math
import numpy as np
import matplotlib.pyplot as plt
def func(x): return 1/(math.sqrt(x))
while True:
    try:
        print(f"y={func(float(input('Iveskite x: '))):.3f}")
        break
    except ValueError:
        print("Klaida: ivestas ne skaicius")
    except ZeroDivisionError:
        print("Klaida: dalyba is nulio negalima")
    except Exception as e:
        print(f"Klaida: {e}")

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
tetr(2)

