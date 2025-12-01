# ts will be implemented to m9_utils in some or other way

global thrs_statu

import time
from threading import Thread


def thr(txt="", wait=0.02, thr_num=int()):
    global thrs_statu
    for a in txt:
        while thrs_statu[thr_num] == 1:
            continue
        thrs_statu[thr_num] = 0
        time.sleep(wait)
        print(f"\r{a}", end="", flush=True)
        thrs_statu[thr_num] = 1
        try:
            thrs_statu[thr_num + 1] = 0
        except IndexError:
            thrs_statu[0] = 0


def SIMPLE(text="abcdefg", wait=0.2, dir="mid", weird_silly_line_break_wave=False):
    global thrs_statu

    if weird_silly_line_break_wave:
        tgl = 0
        texc = text
        text = ""
        for i in texc:
            text += f"{i}\n" if tgl == 1 else f"{i}"
            tgl = 1 - tgl

    textsp = []
    if "\n" in text:
        textsp = text.split("\n")
    else:
        textsp.append(text)

    ct = 0

    frames = []
    for _ in textsp:
        frames.append([])

    thrs_statu = [0]
    for _ in textsp:
        if len(thrs_statu) > len(textsp): break
        thrs_statu.append(1)

    for tex in textsp:

        length = len(tex)
        mid = length // 2

        if dir.lower() == str.lower("mid"):

            if length % 2 == 0:
                start = mid - 1
                end = mid + 1
            else:
                start = mid
                end = mid + 1

            while start >= 0 and end <= length:
                # hidden chars on left  -> spaces
                left_hidden = start
                # hidden chars on right -> spaces
                right_hidden = length - end

                row = " " * left_hidden + tex[start:end] + " " * right_hidden
                frames[ct].append(row)

                start -= 1
                end += 1

        if dir.lower() == str.lower("ltr"):
            start = 0
            end = 0

            while start >= 0 and end <= length:
                # hidden chars on right -> spaces
                right_hidden = length - end

                row = tex[start:end] + " " * right_hidden
                frames[ct].append(row)

                end += 1

        if dir.lower() == "rtl":
            start = length - 1
            end = 0

            while start >= 0 and end <= length:
                # hidden chars on left  -> spaces
                left_hidden = abs(end - start)

                row = " " * left_hidden + tex[start]
                frames[ct].append(row)

                start -= 1

        ct += 1

    # print frames slowly
    ct2 = 0
    n = "\n"
    for r in frames:
        p = Thread(target=thr(r, wait, ct2))
        p.start()
        ct2 += 1

    print()


SIMPLE("+++ initializing insanity engine +++\ntbf ts fire", 0.02, "rtl")
