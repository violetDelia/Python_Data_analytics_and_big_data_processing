# !/usr/bin/python
# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt

lines = plt.plot(#[1, 2, 3, 4], [1, 4, 9, 16],
                 [1, 2, 3, 4]*2, [1, 4, 9, 16]*2 )
plt.axis([0, 9, 0, 20])
lines[0].set_antialiased(False)

plt.setp(lines, "color", "r", "linewidth", 2.0)
plt.show()


