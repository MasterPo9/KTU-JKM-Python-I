"""
Uses matplotlib to easily draw a plot
\use update mode
"""

import matplotlib.pyplot as plt


def drwplt(style=0, mode: str = "normal", x=None, y=None, lbl1="", title: str = "", xlabel: str = "", ylabel: str = "",
           sx=None,
           sy=None, lbl2=""):
    if y is None:
        y = []
    if x is None:
        y = []

    tmpy, tmpx = [], []

    if style == 0:
        pass
    if style == 1:
        plt.style.use('dark_background')
    if style == 2:
        plt.style.use('seaborn')

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    if mode == "normal":
        if not (sx and sy):
            plt.plot(x, y, label=lbl1)
            plt.legend()
        else:
            plt.plot(x, y, label=lbl1)
            plt.plot(sx, sy, label=lbl2)
            plt.legend()


    elif mode == "scatter":
        if not (sx and sy):
            plt.scatter(x, y, label=lbl1)
            plt.legend()
        else:
            plt.scatter(x, y, label=lbl1)
            plt.scatter(sx, sy, label=lbl2)
            plt.legend()

    elif mode == "bar":
        if not (sx and sy):
            plt.bar(x, y, label=lbl1)
            plt.legend()
        else:
            plt.bar(x, y, label=lbl1)
            plt.bar(sx, sy, label=lbl2)
            plt.legend()

    plt.show()
