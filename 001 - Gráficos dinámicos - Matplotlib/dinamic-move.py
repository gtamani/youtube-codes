import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import random, numpy as np

fig, ax = plt.subplots()
line, = ax.plot(0)


time_values = [135]
seconds = 0

def update(x):
    global seconds

    ax.clear()

    seconds += 1
    last = time_values[-1]
    last *= random.choice(np.linspace(0.98,1.02,20))

    time_values.append(last)

    from_ = seconds - 100 if seconds >= 100 else 0
    ax.set_xlim(from_,seconds)


    line, = ax.plot(time_values)

    plt.title("Cotización GGAL")
    return line,

animation = FuncAnimation(fig,func=update,interval=50)
plt.show()

