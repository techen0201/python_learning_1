import numpy as np
from matplotlib import pyplot as plt
import math
x=np.arange(0,math.pi*2,0.05)
fig=plt.figure()
axes1=fig.add_axes([0.1,0.1,0.8,0.8])
axes2=fig.add_axes([0.55,0.55,0.3,0.3])
axes1.plot(x,np.sin(x),'r')
axes2.plot(x,np.cos(x))
axes1.set_title('sin')
axes2.set_title('cos')
plt.show()
