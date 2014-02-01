# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 22:24:45 2014

@author: samantha
"""

import numpy as np
from scipy.optimize import curve_fit

# Creating a function to model and create data
def func(x, a, b):
    return a * x + b

# Generating clean data
x = np.linspace(0,10,100)
y = func(x,1,2)

# Adding noise
yn = y + 0.9 * np.random.normal(size=len(x))

# using curve_fit
popt, pcov = curve_fit(func, x, yn)

#popt == best fit values for the model func

print(popt)