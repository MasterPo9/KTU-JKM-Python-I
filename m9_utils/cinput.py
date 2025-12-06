"""
Cinput usage:
cinput(a="enter the text to be displayed before input", Force_Number_Input=False, Float_Force_Extension=False, Preferred_Value_Amount=0, Force_Preferred_Value_Amount=False, DEBUG=False, LTSEFC="", BOLTS=False, RFoBOLTL=0, PEI3o1="", PMP=0.1, VIR=range(1, 11), BOVIRV = False, RNPL = False)
Force_Number_Input essentially blocks all non-number input
Float_Force_Extension only works when Force_Number_Input is True, enabling "." to be used, to make floats
Preferred_Value_Amount allows a preferred Value amount, from which, if the list is +-{10% of the Preferred Value Amount Variable} larger, or smaller (by length), it will be blocked; if 0 then it won't be enabled
Force_Preferred_Value_Amount forces the above to the exact value amount.
LTSEFC means "List Too Short Error Feedback Custom". If none (""), it won't be used, and will use a preset error message.
BOLTS means, not literally bolts, but "Block On List Too Short".
RFoBOLTL means "Return Feedback or Block On List Too Long". This requires an integer input:
0 - disabled
1 - return feedback (no block)
2 - block with no feedback
3 - block and return feedback (either preset if PEI3o1 not set or custom)
PEI3o1 means "Previous Extension If 3 or 1". Allows setting of custom feedback if RFoBOLTL is 3 or 1
PMP means "Plus Minus Percent". 0.1 is 10%.
VIR means "Value Input Range". If empty (None), this feature will be disabled. Use by using range(a, b).
BOVIRV means "Block On Value Input Range Violation". False will just delete single values not in range. True will block the entire output by restarting the input process.
RNPL means "Return Not Processed List". This returns a list before range filtering. The return output will be very diffrent when using this, as it will output 2 lists,
the first being the formatted list and second being the Not Processed list.
"""

list_of_all_letters = [chr(i) for i in range(32, 33)] + [chr(46)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in
                                                                                                       range(97, 123)]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


def cinput(a="Input: ", Force_Number_Input=False, Float_Force_Extension=False, Preferred_Value_Amount=0,
           Force_Preferred_Value_Amount=False, DEBUG=False, LTSEFC="", BOLTS=False, RFoBOLTL=0, PEI3o1="",
           PMP=0.2, VIR=None, BOVIRV=False, RNPL=False):  # if Preferred Value Amount is 0, then it will essentially be disabled.
    if Float_Force_Extension and not Force_Number_Input:
        Float_Force_Extension = False

    if Preferred_Value_Amount == 0 and Force_Preferred_Value_Amount:
        Force_Preferred_Value_Amount = False

    if RFoBOLTL not in (1, 3):
        PEI3o1 = ""

    TRIGGER_REINPUT=False

    list_of_all_letters__type_ns = list_of_all_letters
    try:
        list_of_all_letters__type_ns.remove(chr(32))
    except:
        pass

    MODE = MODE1 = MODE2 = ""

    FLOATMODE = False
    INTMODE = False

    INTMODE_PERM_FALSE = False
    if DEBUG: print("Debug Enabled!")

    while True:

        it_paz = input(f"{a}")

        digits_collected = []
        digits_nl_lenght = 0
        digits_rletter = ""

        MODE = None

        for i in it_paz:
            if i in numbers:
                INTMODE = True
                MODE2 = MODE1
                MODE1 = MODE
                MODE = "NUM"
                digits_nl_lenght += 1
                digits_rletter += str(i)
                if DEBUG: print(f"\r\x1b[K{digits_rletter};{MODE}←{MODE1}←{MODE2}; {digits_nl_lenght}")
            elif i in list_of_all_letters__type_ns:
                if Force_Number_Input and not Float_Force_Extension: continue
                INTMODE = False
                MODE2 = MODE1
                MODE1 = MODE
                MODE = "LTR"
                if i == "." and MODE1 == "NUM":
                    MODE2 = MODE1
                    MODE1 = MODE
                    MODE = "NUM"
                    digits_nl_lenght += 1
                    digits_rletter += str(i)
                    INTMODE = True
                    FLOATMODE = True
                    if Force_Number_Input and Float_Force_Extension: continue
                elif (MODE1 == "SEP" or MODE2 == "SEP") and i == ".":
                    MODE = "SEP"
                    continue
                else:
                    if Force_Number_Input and Float_Force_Extension: continue
                    INTMODE_PERM_FALSE = True
                    if DEBUG: print("Enabled Permanent INTMODE")
                    digits_nl_lenght += 1
                    digits_rletter += str(i)

                if DEBUG: print(f"\r\x1b[K{digits_rletter};{MODE}←{MODE1}←{MODE2}; {digits_nl_lenght}")
            else:
                if MODE != "SEP":
                    digits_nl_lenght = 1
                    digits_collected.append(digits_rletter)
                    if DEBUG: print(
                        f"Appended before changing of MODE(prev {MODE}←{MODE1}←{MODE2}) to SEP({digits_rletter})")

                MODE2 = MODE1
                MODE1 = MODE
                MODE = "SEP"

                digits_rletter = ""
                if DEBUG: print(f"\r\x1b[K{digits_rletter};{MODE}←{MODE1}←{MODE2}; {digits_nl_lenght}")

        if digits_rletter:
            digits_collected.append(digits_rletter)
        if RNPL: og_digits_collected = digits_collected
        if DEBUG: print(f"Gotten result: {digits_collected}")

        rem_empt_res = []
        ct = 0
        cte = 0
        ctne = 0
        for i in digits_collected:
            ct += 1
            if i == "":
                cte += 1
                if DEBUG: print(f"Found empty value in list (#l-{ct}/#e-{cte})")
                continue
            else:
                rem_empt_res.append(i)
                ctne += 1
                if DEBUG: print(f"Found not empty value in list (#l-{ct}/#ne-{ctne})")
        digits_collected = rem_empt_res

        if Force_Preferred_Value_Amount and len(digits_collected) != Preferred_Value_Amount:
            if RFoBOLTL == 1 or RFoBOLTL == 3:
                if PEI3o1:
                    print(PEI3o1)
                else:
                    print(f"List Doesnt Match required length ({Preferred_Value_Amount})!")
            if RFoBOLTL == 0:
                print(f"List Doesnt Match required length ({Preferred_Value_Amount})!")
            continue

        if (len(digits_collected) > Preferred_Value_Amount * (1 + PMP) or len(
                digits_collected) < Preferred_Value_Amount * (
                    1 - PMP)) and Preferred_Value_Amount != 0 and not Force_Preferred_Value_Amount:
            if len(digits_collected) > Preferred_Value_Amount * (1 + PMP):
                if RFoBOLTL == 1 or RFoBOLTL == 3 or RFoBOLTL == 0:
                    if PEI3o1 and RFoBOLTL != 0:
                        print(PEI3o1)
                    elif RFoBOLTL == 0:
                        print("List is too long!")
                    else:
                        print("List is too long!")
                    if RFoBOLTL == 2 or RFoBOLTL == 3:
                        continue

            if len(digits_collected) < Preferred_Value_Amount * (1 - PMP):
                if LTSEFC:
                    print(LTSEFC)
                else:
                    print("List is too short!")
                if BOLTS:
                    continue

        # if RNPL:
        #     og_digits_collected = digits_collected
        #     if DEBUG: print("Set og_digits_collected=", og_digits_collected)

        if VIR:
            for i in digits_collected:
                if int(i) not in VIR:
                    if not BOVIRV:
                        digits_collected.remove(i)
                        if DEBUG: print(f"Found invalid digit, out of provided range ({VIR}): {i}")
                    else:
                        TRIGGER_REINPUT = True
                        break

        if TRIGGER_REINPUT:
            continue

        break

    if not INTMODE_PERM_FALSE:
        it_int = []
        for i in digits_collected:
            if INTMODE and not FLOATMODE:
                it_int.append(int(i))
            elif INTMODE and FLOATMODE:
                it_int.append(float(i))
        if not RNPL:
            return it_int
        elif RNPL:
            return [it_int, og_digits_collected]

    else:
        if not RNPL:
            return digits_collected
        elif RNPL:
            return [digits_collected, og_digits_collected]
