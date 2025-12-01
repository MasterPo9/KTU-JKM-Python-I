def SIMPLE():
    text = "+++INITIALIZING+++"
    spacing = " "
    length = len(text)
    selected: list[list[int]] = []
    res = [""] * length

    # Build the index selection
    for i in range(length):
        if i == 0 and length % 2 != 0:
            indices = [length // 2, length // 2 + 1]
        elif i == 0 and length % 2 == 0:
            indices = [length // 2]
        elif i > 0 and length % 2 != 0:
            indices = [length // 2 - i, length // 2 + 1 + i]
        else:  # i > 0 and length % 2 == 0
            indices = [length // 2 - i, length // 2 + i]

        # Clamp indices to valid range
        indices = [max(0, min(length - 1, idx)) for idx in indices]
        selected.append(indices)

    # Build output strings
    for ct, indices in enumerate(selected):
        pad = spacing * (length // 2 - len(indices) // 2)
        for j in indices:
            res[ct] += pad + text[j] + pad

    # Print the pyramid
    for row in res:
        print(f"\r{row}")


SIMPLE()
