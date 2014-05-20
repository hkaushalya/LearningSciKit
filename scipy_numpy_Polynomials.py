# -*- coding: utf-8 -*-
"""
@author: samantha
3.4.1 Polynomials
"""
import numpy as np
from matplotlib import pyplot as plt

#%% 3x^2+2x-1
p = np.poly1d([3, 2, -1])
p(0)
p.roots
p.order

#%%
x = np.linspace(0, 1, 20)
np.random.seed(1234)
y = np.cos(x) + 0.3 * np.random.rand(20)
p = np.poly1d(np.polyfit(x, y, 3))
t = np.linspace(0, 1, 200)
plt.plot(x, y, 'o', t, p(t), '-')
# plt.plot(x, y)
