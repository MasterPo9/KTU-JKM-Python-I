import math
import numpy as np
import time
import os

list_of_all_letters =[chr(i) for i in range(32, 33)] + [chr(46)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
text=input("Iveskite teksta: ")
color=str(input("Iveskite teksto ir fono spalva naudodami 1 raides HEX(pvz 0F yra juodas fonas ir baltos raides): "))
os.system(f'color {color}')

if text.__contains__("[]\{\}()<>/\\'\;:|`~!@#$%^&*-+=_1234567890,"):
    print("Pastaba: ivestas tekstas turi specialiu simboliu, kurie nebus animuoti")
    time.sleep(2)
x=""
start=time.time()
for i in range(0, len(text)):
    for a in range(0, len(list_of_all_letters)):
        print(x+list_of_all_letters[a])
        if text[i]==list_of_all_letters[a]:
            break
        time.sleep(0.001)
    x+=text[i]
    if text==x:
            break
print(x)
end=time.time()
time.sleep(2)
print(f"Uztruko: {end-start:.1f} sekundziu\nBuvo spaudzdinama {(len(text)/(end-start)):.2f} radziu per sekunde")
os.system('color 07')