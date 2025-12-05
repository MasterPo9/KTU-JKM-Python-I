import math
import time

import matplotlib.pyplot as plt

plt.ion()

fig, ax = plt.subplots()
line, = ax.plot([], [])

x = []
y = []

for i in range(100000):
    x.append(i)
    if i != 0:
        try:
            y.append(math.log2(y[i - 1]))
        except:
            y.append(0)
    else:
        y.append(1000)

    line.set_xdata(x)
    line.set_ydata(y)

    ax.relim()
    ax.autoscale_view()

    fig.canvas.draw()
    fig.canvas.flush_events()

    time.sleep(0.01)
