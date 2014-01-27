# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 13:14:40 2014

@author: samantha
"""

import numpy as np
import scipy as sp

p = poly1d([3,4,5])
print(p)
#%% eval
p(0.5)
#%% roots
p.r
#%%add/sub/mul
print p*p


#%% vectorizing functions
def addsubtract(a,b):
    if a > b:
        return a - b
    else:
        return a + b

vec_addsubtract = vectorize(addsubtract)
sol = vec_addsubtract([20,30,40],[2,3,4])
print(sol)

#%% type handling
x = 1+6i
class(x)
type(x)

np.cast['f'](np.pi)

#%% integration
import scipy.integrate
help(integrate)

pol1 = sp.poly1d([1,1])
#res = integrate.quad()

#%% interpolation

from scipy.interpolate import interp1d

x = np.linspace(0,10,10)
y = np.cos(-x**2/8.0)
f = interp1d(x,y)
f2 = interp1d(x,y, kind='cubic')
xnew = np.linspace(0,10,40)
import matplotlib.pyplot as plt
plt.plot(x,y,'o',xnew,f(xnew), ':', xnew, f2(xnew),'^')
plt.legend(['data','linear','cubic'], loc='best')
plt.show()

#%% MV data interpolation (griddata)


