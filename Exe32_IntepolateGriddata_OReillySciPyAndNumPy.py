# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 16:32:13 2014

@author: samantha

Interpolating grid data

"""

import numpy as np
from scipy.interpolate import griddata

# Define the function
ripple = lambda x, y: np.sqrt(x**2 + y**2) + np.sin(x**2 + y**2)
