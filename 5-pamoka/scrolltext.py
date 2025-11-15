"""
A simple scrolling text animation in the console.
Imports: time, os
Function: scroll(text, color='0F', speed=0.001)
may contain other useful functions"""
#no find other functions in my github: https://github.com/MasterPo9/KTU-JKM-Python-I
def cinput(a="Input: ", contains_sp=False, contains_cm=False, contains_both=False):
    it_paz=input(f"{a}")

    for i in range(0, len(it_paz)):
        if it_paz[i] == " ":
            contains_sp=True
        if it_paz[i] == ",":
            contains_cm=True                                #auto detect format (split by spaces, or commas)

    if contains_cm and contains_sp: 
        contains_both=True
        contains_cm, contains_sp=False, False               #or if both are used, split by both

    if contains_sp:
        it=it_paz.split(" ")

    if contains_cm:
        it=it_paz.split(",")

    if contains_both:
        it=it_paz.split(", ")  
    return it