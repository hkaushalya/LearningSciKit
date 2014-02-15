# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 20:06:10 2014

@author: samantha
"""
import numpy 

#Euler Problem 1.

a = numpy.arange(1,1000)

# Select the multiples of 3 or 5

a = a[(a % 3 == 0) | (a % 5 ==0)]
print a[:10]

# sum the array elements
print a.sum()