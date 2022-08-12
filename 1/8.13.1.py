import matplotlib.pyplot as plt
import numpy as np

POINTS = 100
sin_list = [0] * POINTS
indx = 0
# fig, ax = plt.subplots()
while True:
    if indx == 40:
        indx = 0
    indx += 1
    # 更新绘图数据
    sin_list = sin_list[1:] + [np.sin((indx / 20) * np.pi)]
    # 显示时间
    plt.pause(0.01)
    # 清除上一次显示
    plt.cla()
    plt.plot(sin_list)
    #plt.show()如果放在这个位置就会卡住
plt.show() #放在最后不会影响之后的代码执行