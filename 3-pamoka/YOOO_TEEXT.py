import math
import numpy as np
import time
import os
import scrolltext as st

text=input("Iveskite teksta: ")
color=str(input("Iveskite teksto ir fono spalva naudodami 1 raides HEX(pvz 0F yra juodas fonas ir baltos raides): "))
speed=float(input("Iveskite spaudimo greiti (mazesnis skaicius yra greiciau, pvz 0.001): "))
start=time.time()
st.scroll(text, color, speed)
end=time.time()
time.sleep(2)
print(f"Uztruko: {end-start:.1f} sekundziu\nBuvo spaudzdinama {(len(text)/(end-start)):.2f} radziu per sekunde")
os.system('color 07')