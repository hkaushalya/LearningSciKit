# -*- coding: utf-8 -*-
"""
@author: samantha

"""

# Broadcasting
import numpy as np

a = np.tile(np.arange(0, 40, 10), (3,1)).T
a
b = np.array([0, 1, 2])
b
a + b

#%%
a = np.ones((4,5))
a
a[0] = 2 # assign an array of dimension 0 to an array of dimension 1
a

#%% useful trick
a = np.arange(0, 40, 10)
a
a.shape
a = a[:, np.newaxis]    # adds a new axis -> 2D array
a
a.shape
b
a+b