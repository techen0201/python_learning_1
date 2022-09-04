from time import sleep
import numpy as np
from matplotlib import pyplot as plt
import math
x=np.arange(-1.81,1.81,0.01)
plt.ion() #打开交互模式
figure, ax = plt.subplots()
lines, = plt.plot([], [], 'r')
for a in np.arange(0.1,100,0.1):
    y=(x**2)**(1/3)+0.9*np.power(3.3-x**2,0.5)*np.sin(a*math.pi*x)
    lines.set_xdata(x)
    lines.set_ydata(y)
    ax.relim()
    ax.autoscale_view()
    figure.canvas.draw_idle()
    figure.canvas.flush_events()
    sleep(0.0001)
