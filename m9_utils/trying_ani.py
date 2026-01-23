# ts will be implemented to m9_utils in some or other way
# SIMPLE("+++ initializing insanity engine +++", 0.02, "rtl")
# print(f'\nyou will get {gambling([f"{LIGHT_WHITE}{FAINT}zero{RESET}", f"{LIGHT_CYAN}one{RESET}", f"{CYAN}two{RESET}", f"{BLUE}three{RESET}", f"{LIGHT_GREEN}four{RESET}", f"{GREEN}five{RESET}", f"{LIGHT_PURPLE}six{RESET}", f"{PURPLEC}{BOLD}seven{RESET}", f"{BLINK}{RED}{REDBG}{BOLD}{CURLYUNDERLINE}ten{RESET}"], [10, 5, 2.5, 1.25, 0.625, 0.3125, 0.15625, 0.078125, 0.0390625])} cents')
import colorsys
import time
from threading import Thread

BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
CURLYUNDERLINE = "\033[4:3m"
OVERLINE = "\033[53m"
BLINK = "\033[5m"
FBLINK = "\033[6m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
FRAKTUR = "\033[20m"
END = "\033[0m"
PURPLEC = "\033[38;2;105;19;223m"
CYANC = "\033[38;2;119;185;221m"
REDBG = "\033[0;41m"
RESET = "\x1b[0m"


def thr(txt="", wait=0.02):
    for a in txt:
        time.sleep(wait)
        print(f"\r{a}", end="", flush=True)


def SIMPLE(text="abcdefg", wait=0.2, dir="mid", weird_silly_line_break_wave=False):
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
        p = Thread(target=thr(r, wait))
        p.start()
        ct2 += 1

    print()


def closeness(a, b):
    return 1.0 if a == b else 1 - abs(a - b) / max(a, b)


def gambling(both=None, weights=None):
    if weights is None:
        weights = []
    if both is None:
        both = []
    import random
    import colorama
    import re
    import time

    ansi_re = re.compile(r'\x1b\[[0-9;]*m')

    def visible_len(s: str) -> int:
        return len(ansi_re.sub('', s))

    # precompute longest visible length (important)
    max_vis_len = max(visible_len(x) for x in both)

    chsn1 = chsn0 = chsnn1 = "placeholder"
    x = random.randrange(20, 30)
    max_val = len(both) * x
    width = len(str(max_val))
    weightsum = sum(weights)
    weightintlenght = len(str(int(weightsum)))
    weightdeclenght = len(str(weightsum)) - weightintlenght
    spc = " "
    spc_i = "-"

    for i in range(1, len(both) * x):
        chsn1 = chsn0
        chsn0 = chsnn1
        chsnn1 = random.choices(both, weights=weights, k=1)[0]

        try:
            selected_nx = both.index(chsn0)
        except ValueError:
            selected_nx = 0

        print(colorama.ansi.clear_screen() + colorama.ansi.Cursor.POS(0, 0), end="")

        print(
            f"   {(((max_vis_len - visible_len(chsnn1)) // 2) * spc) + chsnn1 + (((max_vis_len - visible_len(chsnn1)) // 2) * spc)}   \n"
            f"---{(((max_vis_len - visible_len(chsn0)) // 2) * spc_i) + chsn0 + (((max_vis_len - visible_len(chsn0)) // 2) * spc_i)}---\n"
            f"   {(((max_vis_len - visible_len(chsn1)) // 2) * spc) + chsn1 + (((max_vis_len - visible_len(chsn1)) // 2) * spc)}   \n\n"
            f"({i:0{width}d}/{len(both) * x})\nCurrent roll weight: {weights[selected_nx]}\nChance to get this value: {weights[selected_nx] / weightsum * 100:.2f}%"
        )

        time.sleep(0.1 * ((closeness(i, max_val)) ** 2 * 10))

    # final roll
    chsn1 = chsn0
    chsn0 = chsnn1
    chsnn1 = random.choices(both, weights=weights, k=1)[0]

    try:
        selected_nx = both.index(chsn0)
    except ValueError:
        selected_nx = 0

    print(colorama.ansi.clear_screen() + colorama.ansi.Cursor.POS(0, 0), end="")

    print(
        f"   {(((max_vis_len - visible_len(chsnn1)) // 2) * spc) + chsnn1 + (((max_vis_len - visible_len(chsnn1)) // 2) * spc)}   \n"
        f"---{(((max_vis_len - visible_len(chsn0)) // 2) * spc_i) + chsn0 + (((max_vis_len - visible_len(chsn0)) // 2) * spc_i)}---\n"
        f"   {(((max_vis_len - visible_len(chsn1)) // 2) * spc) + chsn1 + (((max_vis_len - visible_len(chsn1)) // 2) * spc)}   \n\n"
        f"({(len(both) * x):0{width}d}/{len(both) * x})\nCurrent roll weight: {weights[selected_nx]}\nChance to get this value: {weights[selected_nx] / weightsum * 100:.2f}%"
    )

    time.sleep(0.1 * 1.1 ** 2 * 10)

    return chsn0


def rainbow(text="Hello World!", speed=0.01, step=0.0025, mode=2):
    import time
    import colorsys
    h = 0.0
    sh = 0.0
    while True:
        if mode == 1:
            r, g, b = colorsys.hsv_to_rgb(h, 1, 1)
            r, g, b = int(r * 255), int(g * 255), int(b * 255)

            print(f"\r\033[38;2;{r};{g};{b}m{text}\033[0m", end="", flush=True)

            h += step
            if h >= 1.0:
                h = 0.0

        elif mode == 2:
            print("\r", end="", flush=True)
            ct = 0
            for i in text:
                if ct == 0:
                    if sh: h = sh + step
                    sh = h
                    if sh >= 1.0:
                        sh -= 1.0

                r, g, b = colorsys.hsv_to_rgb(h, 1, 1)
                r, g, b = int(r * 255), int(g * 255), int(b * 255)

                print(f"\033[38;2;{r};{g};{b}m{i}\033[0m", end="", flush=True)
                # remove all text between "#" to enable debug#print(f"DBG: i:{i};sh:{sh};h:{h};ct:{ct};r/g/b:{r}/{g}/{b}", end="", flush=True)

                h += step
                if h >= 1.0:
                    h = 0.0
                ct += 1
        time.sleep(speed)


def generate_gradient(text: str = "Hello World!", hcolor1: float = 0.65, hcolor2: float = 0.775, mode_override=0):
    # I will only support hue as i don't care about those other ones (i won't need them anyway)
    # oh yeah then i don't need to enter other values, only hue then.

    diff = hcolor2 - hcolor1
    bdiff = hcolor1 + (1 - hcolor2)
    step_size = abs(diff) / len(text)
    b_step_size = abs(bdiff) / len(text)
    h = hcolor1
    if bdiff < diff and not mode_override == 2 or mode_override == 1:  # do backwards gradient(reaching 0.0 and overlapping to 1, then reaching whatever hcolor2 is) if it is closer
        for i in text:
            r, g, b = colorsys.hsv_to_rgb(h, 1, 1)
            r, g, b = int(r * 255), int(g * 255), int(b * 255)
            ph = h
            h -= b_step_size
            if h > 1.0:
                h = 0.0
            elif h < 0.0:
                h = 1.0 - abs(h)
            print(f"\033[38;2;{r};{g};{b}m{i}\033[0m", end="", flush=True)
    elif not mode_override == 1 or mode_override == 2:
        for i in text:
            r, g, b = colorsys.hsv_to_rgb(h, 1, 1)
            r, g, b = int(r * 255), int(g * 255), int(b * 255)
            ph = h
            h += step_size
            if h > 1.0:
                h = 0.0 + abs(h - 1)
            elif h < 0.0:
                h = 1.0 - abs(h)
            print(f"\033[38;2;{r};{g};{b}m{i}\033[0m", end="", flush=True)


generate_gradient()
# SIMPLE("+++ initializing insanity engine +++", 0.02, "rtl")
# print(f'\nyou will get {gambling([f"{LIGHT_WHITE}{FAINT}zero{RESET}", f"{LIGHT_CYAN}one{RESET}", f"{CYAN}two{RESET}", f"{BLUE}three{RESET}", f"{LIGHT_GREEN}four{RESET}", f"{GREEN}five{RESET}", f"{LIGHT_PURPLE}six{RESET}", f"{PURPLEC}{BOLD}seven{RESET}", f"{BLINK}{RED}{REDBG}{BOLD}{CURLYUNDERLINE}ten{RESET}"], [10, 5, 2.5, 1.25, 0.625, 0.3125, 0.15625, 0.078125, 0.0390625])} cents')
