import msvcrt
import time

from plyer import notification

NSET = True

rh, rm, rs = 0, 0, 0

with open("REM.txt", "r") as f:
    try:
        rh, rm, rs = [int(i) for i in f.read().split(":")[:3]]
        NSET = False
    except:
        NSET = True


def setrem(rh, rm, rs):
    frm = f"\033[2J\033[H{int(h):02}:{int(m):02}:{int(s):02} — PS INP | SET REM"
    print(frm)
    try:
        with open("REM.txt", "w") as f:
            f.write(input("Enter Reminder time, in format HH:MM:SS "))
        with open("REM.txt", "r") as f:
            rh, rm, rs = [int(i) for i in f.read().split(":")[:3]]

        NSET = False
    except:
        NSET = True
    return rh, rm, rs


while True:
    h = (time.time() / 3600 + 2) % 24
    m = h * 60 % 60
    s = m * 60 % 60
    lftm = (rh - int(h)) * 60 + (rm - int(m))
    lfts = rs - s
    if lfts < 0:
        lftm -= 1
        lfts = 60 - abs(lfts)
    if lftm < 0:
        lftm %= 1440
    if NSET:
        frm = f"\033[2J\033[H{int(h):02}:{int(m):02}:{int(s):02} | REM NSET\nPress R to set a reminder"
    else:
        frm = f"\033[2J\033[H{int(h):02}:{int(m):02}:{int(s):02} | REM {rh:02}:{rm:02}:{rs:02} (LFT {int(lftm)}:{int(lfts):02})\nPress R to set a reminder"
        if int(h) == rh and int(m) == rm and int(s) == rs:
            notification.notify(
                title="Python",
                message="This is a notification, for your set reminder",
                timeout=5
            )

    if msvcrt.kbhit():
        key = msvcrt.getch().decode()
        if key == "r":
            rh, rm, rs = setrem(rh, rm, rs)

    time.sleep(0.05)
    print(frm, end="", flush=True)
