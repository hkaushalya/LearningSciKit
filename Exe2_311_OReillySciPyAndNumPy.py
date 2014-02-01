# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:06:41 2014

@author: samantha

SciPy and NumPy
"""

import numpy as np
from scipy.optimize import curve_fit

# least-squares fit to a Gaussian profile, a non-linear function:
# a * exp (-(x-mu)^2/2*sigma^2)

# creating a function to model and create data
def func(x, a, b, c):
    return a * np.exp(-(x-b)**2/(2*c**2))

# Generating clean data
x = np.linspace(0,10,100)
y = func(x,1,5,2)

# Adding noise
yn = y + 0.2 * np.random.normal(size=len(x))

# using curve_fit
popt, pcov = curve_fit(func, x, yn)

# popt == best fit values for the model func
# pcov == covariant matrix! quality of fit: diagonal elements are the variances
#         for each parameter.

print(popt)


# best fit
fit_a = popt[0]
fit_b = popt[1]
fit_c = popt[2]
fit_yn = func(x, fit_a, fit_b, fit_c)

import pylab as pl

pl.figure(figsize=(8,6), dpi=80)
pl.scatter(x,yn, color='green', label='Gaussian smeared data')
pl.plot(x,y,color='red', linestyle='-', linewidth=2.5, label='Original line')
pl.plot(x, fit_yn, linestyle='-', color='blue', linewidth=2.5, label='Fitted line')
pl.legend(loc='upper left')
#pl.plot(x, fit_yn)
pl.show()

# Save figure using 72 dots per inch
savefig("Exe2_311.png", dpi=72)