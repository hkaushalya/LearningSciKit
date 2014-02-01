# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:06:41 2014

@author: samantha

Double-Gaussian fit
"""

import numpy as np
from scipy.optimize import curve_fit


# Two-Gaussian model
def func(x, a0, b0, c0, a1, b1, c1):
    return a0 * np.exp(-(x-b0)**2/(2*c0**2))\
            + a1 * np.exp(-(x-b1)**2/(2*c1**2))

# Generating clean data
x = np.linspace(0,20,200)
y = func(x,1,3,1,-2,15,0.5)

# Adding noise
yn = y + 0.2 * np.random.normal(size=len(x))

# when fitting complex functions,providing
# guesses may yeild better results
guesses = [1,3,1,1,15,1]  # second gauss fit would fail!

# using curve_fit
popt, pcov = curve_fit(func, x, yn, p0=guesses)

# popt == best fit values for the model func
# pcov == covariant matrix! quality of fit: diagonal elements are the variances
#         for each parameter.

print(popt)


# best fit
fit_a0 = popt[0]
fit_b0 = popt[1]
fit_c0 = popt[2]
fit_a1 = popt[0]
fit_b1 = popt[1]
fit_c1 = popt[2]

fit_yn = func(x, fit_a0, fit_b0, fit_c0, fit_a1, fit_b1, fit_c1)

import pylab as pl

pl.figure(figsize=(8,6), dpi=80)
pl.scatter(x,yn, color='green', label='Gaussian smeared data')
pl.plot(x,y,color='red', linestyle='-', linewidth=2.5, label='Original line')
pl.plot(x, fit_yn, linestyle='-', color='blue', linewidth=2.5, label='Fitted line')
pl.legend(loc='upper right')
#pl.plot(x, fit_yn)
pl.show()

# Save figure using 72 dots per inch
savefig("Exe3_311.png", dpi=72)