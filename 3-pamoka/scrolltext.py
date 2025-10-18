"""
A simple scrolling text animation in the console.
Imports: time, os
Function: scroll(text, color='0F', speed=0.001)"""
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
