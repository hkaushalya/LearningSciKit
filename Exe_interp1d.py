# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 17:00:03 2014

@author: samantha
"""

import scipy.interpolate
import numpy
from pylab import plot, arange, figure, show
from scipy.interpolate import interp1d

y= numpy.load('sample_data.txt')
x=arange(len(y))

figure()
plot(x,y)
show()

class MyInterp1d(interp1d):
    def plot(self):
        figure()
        plot(self.x, self.y)
        show()
