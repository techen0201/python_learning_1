import matplotlib.pyplot as plt
import math
import numpy as np
fig=plt.figure()

x=np.arange(0,math.pi*2,0.05)
y=np.sin(x)
ax=fig.add_axes([0,0,1,1])
ax.plot(x,y)
plt.show()