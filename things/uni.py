# read file
with open("hist.txt") as f:
    text = f.read().splitlines(keepends=True)
print(f"[DEBUG] Stored data: {text}")

# first run: no history
if not text:
    plane = input('What plane in WT are you trying to unlock? ')
    rpreq = int(input('Plane RP required: '))
    with open("hist.txt", "w") as f:
        f.write(f"{plane};{rpreq}\n")
    history = []
else:
    plane, rpreq = text[0].strip().split(";")
    rpreq = int(rpreq)
    history = [int(line.strip()) for line in text[1:]]

# get current progress
prog = int(input(f"How much RP currently on {plane}? "))

# append current progress to history
history.append(prog)

# save back to file
with open("hist.txt", "w") as f:
    f.write(f"{plane};{rpreq}\n")
    f.writelines(f"{h}\n" for h in history)

# calculate RP gained today
got = history[-1] - (history[-2] if len(history) > 1 else 0)

# calculate RP gained yesterday
goty = history[-2] - (history[-3] if len(history) > 2 else 0) if len(history) > 1 else 0

print(f"You got {got} RP today.")

diff = goty - got
if goty < got:
    print(f"That's {-diff} RP more than yesterday!")
elif goty > got:
    print(f"That's {diff} RP less than yesterday.")
else:
    print(f"That's the exact same amount as yesterday!")

# calculate daily gains
gains = [history[i] - history[i - 1] for i in range(1, len(history))]

avg = sum(gains) / len(gains) if gains else 0
remaining = rpreq - history[-1]

if avg > 0:
    print(f"ETA: {remaining / avg:.1f} days (avg {avg:.1f}rp per day)")
else:
    print("ETA: ??? (go earn some RP first)")
