# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 14:04:50 2014

@author: samantha
OReilly SciPy and Numpy
3.2 Interpolation

Interpolating noisy data using spline-fitting 
scipy.interpolate.UnivariateSpline
"""

import numpy as np
from scipy.interpolate import UnivariateSpline
import pylab as pl
# dummy data
sample = 30
x = np.linspace(1,10 * np.pi, sample)
y = np.cos(x) + np.log10(x) + np.random.randn(sample)/10

# interpolating data
f = UnivariateSpline(x,y,s=1)
f0 = UnivariateSpline(x,y,s=0)
f10 = UnivariateSpline(x,y,s=10)

xint = np.linspace(x.min(), x.max(), 1000)
yint = f(xint)
yint0 = f0(xint)
yint10 = f10(xint)

pl.figure(figsize=(10,8))
pl.title('Interpolating Noisy Data')
pl.scatter(x,y, color='red')
pl.plot(x,y, color='black',label='Original')
pl.plot(xint,yint, color='grey',linewidth=2, label=('Univariate Interpolation: s='+str(1)) )
pl.plot(xint,yint0, color='cyan',linewidth=2, label='Univariate Interpolation: s=0')
pl.plot(xint,yint10, color='pink',linewidth=2, label='Univariate Interpolation: s=10')

legend(loc='upper left')
pl.show()
savefig('InterpolatingNoisyData.png')