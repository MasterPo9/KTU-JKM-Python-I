"""
A simple scrolling text animation in the console.
Imports: time, os
Function: scroll(text, color='0F', speed=0.001)
may contain other useful functions"""
list_of_all_letters =[chr(i) for i in range(32, 33)] + [chr(46)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
def scroll(text, color='0F', speed=0.001):
    import time
    import os
    os.system(f'color {color}')

    if text.__contains__("[]\{\}()<>/\\'\;:|`~!@#$%^&*-+=_1234567890,"):
        print("Warning: The input text contains special characters that will not be animated")
        time.sleep(2)
    x=""
    start=time.time()
    for i in range(0, len(text)):
        for a in range(0, len(list_of_all_letters)):
            print(x+list_of_all_letters[a])
            if text[i]==list_of_all_letters[a]:
                break
            time.sleep(speed)
        x+=text[i]
        if text==x:
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
    text=""
    for i in range(length):
        text+=list_of_all_letters[int(random.uniform(0, len(list_of_all_letters)))]
    return text

def random_color():
    import random
    hex_chars="0123456789ABCDEF"
    color=""
    for i in range(2):
        color+=hex_chars[int(random.uniform(0, len(hex_chars)))]
    return color

def random_num_list(length=5, min_val=0, max_val=100):
    import random
    num_list=[]
    for i in range(length):
        num_list.append(int(random.uniform(min_val, max_val)))
    return num_list
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

def lmax(a=[]):
    kb=0
    didzc=0
    ct=1
    for i in a:
        kb+=float(i)
        if float(i) >= didzc:
            didzc=float(i)
        ct+=1
    return didzc