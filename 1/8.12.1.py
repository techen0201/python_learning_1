import numpy as np
import matplotlib.pyplot as plt
np_array_2d1=np.arange(0,9).reshape([3,3])
np_array_2d2=np.arange(11,17).reshape([2,3])
#print(np_array_2d1)
#print(np_array_2d2)
np_array_concatenate=np.concatenate([np_array_2d1 ,np_array_2d2],axis=0)
print(np_array_concatenate)
plt.subplot(211)
plt.plot([0,1,2])

plt.show()