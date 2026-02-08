def formatted_time():
    import time
    h = (time.time() / 3600 + 2) % 24
    m = h * 60 % 60
    s = m * 60 % 60

    return f"{int(h)}:{int(m)}:{int(s)}"
