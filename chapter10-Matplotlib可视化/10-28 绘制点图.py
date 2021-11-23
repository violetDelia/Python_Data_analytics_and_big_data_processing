# !/usr/bin/python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np

plt.figure(1)
plt.subplot(211)
plt.plot(np.sin(np.arange(0, 10)), 'b-.')
plt.subplot(212)
plt.plot(np.sin(np.arange(0, 10)), 'r+')
plt.show()

'''
plot绘制点线图的调用方式:
    1.plot([x],y,[fmt],data = None,**kwargs)
    2.plot([x],y,[fmt],[x2],y2,[fmt2],...,**kwargs)
        [fmt]是多字符串组合,用来设置点或线的样式
    3.plot(data,cloco='',marker='')
        同设置line2D相同
'''
'''
line2D属性列表:
'''
'''
fmt参数:
    fmt = '[color][marker][line]'
    1.color
    2.marker
    3.line
'''