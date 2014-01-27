# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 22:21:19 2014

@author: samantha
"""

from scipy import stats
from scipy.stats import norm
print norm.__doc__

print 'bounds of distribution lower: %s, upper: %s' % (norm.a, norm.b)
rv = norm()
dir(rv)