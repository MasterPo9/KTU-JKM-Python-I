import msvcrt

from m9_utils.trying_ani import gambling, LIGHT_WHITE, LIGHT_CYAN, CYAN, BLUE, LIGHT_GREEN, GREEN, LIGHT_PURPLE, \
    PURPLEC, BLINK, RED, REDBG, BOLD, CURLYUNDERLINE, RESET, FAINT

# Grid setup
cols, rows = 20, 10
boxes = [(3, 4), (10, 5), (15, 7)]  # positions of loot boxes
cursor = [0, 0]


def clear():
    print("\033[H\033[J", end="")


def draw():
    print("\033[H", end="")
    for y in range(rows):
        for x in range(cols):
            if [x, y] == cursor:
                print("↑", end="")
            elif (x, y) in boxes:
                print("█", end="")
            else:
                print(" ", end="")
        print()
    if tuple(cursor) in boxes:
        print("\nTooltip: Press SPACE to roll!")


def roll_loot():
    items = [
        f"{LIGHT_WHITE}{FAINT}zero{RESET}",
        f"{LIGHT_CYAN}one{RESET}",
        f"{CYAN}two{RESET}",
        f"{BLUE}three{RESET}",
        f"{LIGHT_GREEN}four{RESET}",
        f"{GREEN}five{RESET}",
        f"{LIGHT_PURPLE}six{RESET}",
        f"{PURPLEC}{BOLD}seven{RESET}",
        f"{BLINK}{RED}{REDBG}{BOLD}{CURLYUNDERLINE}ten{RESET}"
    ]
    weights = [10, 5, 2.5, 1.25, 0.625, 0.3125, 0.15625, 0.078125, 0.0390625]
    result = gambling(items, weights)
    print(f"\nYou got {result}!")


clear()
draw()
while True:
    if msvcrt.kbhit():
        k = msvcrt.getch()
        if k == b'\xe0':  # arrow keys
            k2 = msvcrt.getch()
            if k2 == b'H':
                cursor[1] = max(0, cursor[1] - 1)  # up
            elif k2 == b'P':
                cursor[1] = min(rows - 1, cursor[1] + 1)  # down
            elif k2 == b'M':
                cursor[0] = min(cols - 1, cursor[0] + 1)  # right
            elif k2 == b'K':
                cursor[0] = max(0, cursor[0] - 1)  # left
        elif k == b' ':  # space = roll
            if tuple(cursor) in boxes:
                roll_loot()
                input("Press Enter to continue...")
        elif k in (b'q', b'Q'):
            break
    draw()
