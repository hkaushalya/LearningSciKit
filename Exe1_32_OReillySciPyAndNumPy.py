# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 22:25:20 2014

@author: samantha
OReilly SciPy and Numpy
3.2 Interpolation

scipy.interpolate 
"""

from scipy.interpolate import interp1d
import numpy as np
import pylab as pl

x = np.linspace(0,10*np.pi,20)
y = np.cos(x)

# interpolating data
fl  = interp1d(x,y,kind='linear')
fq  = interp1d(x,y, kind='quadratic') 
fsl = interp1d(x,y, kind='slinear') 
fcu = interp1d(x,y,kind='cubic')

# slinear == spline interpolation of first order
# quadratic == spline interpolation of second oder
# cubic = spline interpolation of third order

# use x.min, x.max to stay withing the boundaries of data.
xint   = np.linspace(x.min(), x.max(), 1000)
yintl  = fl(xint)
yintq  = fq(xint)
yintsl = fsl(xint)
yintcu = fcu(xint)

pl.figure(figsize=(8,6), dpi=80)
pl.title('Interpolation')
pl.scatter(x, y, color='red', label='Data')
pl.plot(xint, yintl, color='magenta', alpha=0.5, label='Linear Interpolation', linewidth=4)
pl.plot(xint, yintq, color='cyan', label='Quadratic Interpolation', linewidth=2)
pl.plot(xint, yintsl, color='black', label='Linear Spline Interpolation', linewidth=1.5)
pl.plot(xint, yintcu, color='grey',alpha=0.5, label='Cubin Spline Interpolation', linewidth=2)
legend(loc='upper left')
savefig('Interpolation.png')


