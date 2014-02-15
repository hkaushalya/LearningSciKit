# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 12:16:11 2014

@author: samantha
Statistics: random sampling
"""

import scipy.stats as stats 
import numpy as np
import pylab as pl

# x = np.random.randn(1000)
# mean = x.mean()
# std = x.std()
# var = x.var()

x = np.linspace(-5,5,1000)
# normal distribution
dist = stats.norm(loc=0, scale=1)  #loc= mean, scale=standard deviation

# Retreiving norm's PDF and CDF
pdf = dist.pdf(x)
cdf = dist.cdf(x)

# Draw out 500 random values from norm
sample = dist.rvs(100000)

#pl.plot(sample)
#pl.hist(pdf, bins=20, range=(-1,1))
#pl.title('pdf/cdf of normal distribution')
#pl.scatter(x, pdf)
#pl.scatter(x, cdf)
#pl.show()

pl.hist(sample, range=(-3,3),bins=60)