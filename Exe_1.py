# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 06:30:25 2014

@author: samantha
"""

import numpy as np
import timeit as ti
#creating an array with 10^7 elements
arr = np.arange(1e7)

# Coverting to list
larr = arr.tolist()

#lists cannot by default broadcast(? what is broadcast)
#This function emulate what an ndarray can do

def list_times(alist, scalar):
    for i, val in enumerate(alist):
        alist[i] = val * scalar
    return alist

# Using IPython's magic timeit
ti.timeit ("","", timer=arr * 1.1)

#ti.timeit (list_times(larr, 1.1))