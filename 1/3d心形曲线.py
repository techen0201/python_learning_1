from time import sleep
import numpy as np
from matplotlib import pyplot as plt
x=np.arange(-3,3,0.01)
y=np.arange(-3,3,0.01)
z=np.arange(-3,3,0.01)
plt.ion() #打开交互模式
figure, ax = plt.subplots()
lines, = plt.plot([],[],[], 'r')
for a in np.arange(-5,5,0.01):
    a=(x**2+ (9/4)*y**2+ z**2- 1)**3- x**2*z**3-(9/80)*y**2*z**3
    lines.set_data(x,y,z)
#   lines.set_ydata(y)
    ax.relim()
    ax.autoscale_view()
    figure.canvas.draw_idle()
    figure.canvas.flush_events()
    sleep(0.0001)
