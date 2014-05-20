# -*- coding: utf-8 -*-
"""
@author: samantha
#3.2.1 Elementwise Operations in Python
"""

import numpy as np
#%% pp. 60: #3.2.1 Elementwise Operations
a = np.array([1,2,3,4])
a + 1
2**a  # 2 to-the-power a
a**2  # a to-the-power 2 (elementwise multiplication)

#%%
j = np. arange(5)
j
2**(j+1) - j

#%% array multiplication is not matrix multiplication

c = np.ones((3,3))
c * c   # NOT matrix multiplication
c.dot(c)   # MATRIX MULTIPLICATION

#%% add even elements with odd elements

a = np.arange(9).reshape(3,3)
b  = np.ones((3,3))

#%% comparisons
a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
a == b
a > b
r = (a == b)
r
#%% array-wise comparisons
a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
c = np.array([1, 2, 3, 4])
np.array_equal(a, b)
np.array_equal(a, c)

#%% logical operations
a = np.array([1, 1, 0, 0], dtype=bool)
b = np.array([1, 0, 1, 0], dtype=bool)
np.logical_or(a, b)
np.logical_and(a, b)

#%% transcendental functions
a = np.arange(5)
print a
print 'sin(a)='
np.sin(a)
np.log(a)
np.exp(a)

#%% transposition
a = np.triu(np.ones((3,3)), 1)
a
a.T
a += a.T
a

#%% 3.2.2 Basic Reductions
# Computing sums
x = np.array([1, 2, 3, 4])
np.sum(x)
x.sum()
#sums by rows and columns
x = np.array([[1, 1], [2, 2]])
x
x.sum(axis=0) # columns (first dimension)
x.sum(axis=1) # rows (second dimension)

x[:,0].sum(), x[:,1].sum() # sum of 1st dim
x[0,:].sum(), x[1,:].sum() # sum of 2nd dim

# higher dimensions
np.random.seed(1234)
x = np.random.rand(2,2,2)
x
x.sum(axis=2)
x.sum(axis=2)[0,1]
x[0,:]
x[0,1,:]
x[0,1,:].sum()

#%% extrema
x = np.array([1,3,2])
x
Minx = x.min()
Minx
Minidx = x.argmin()  #== np.argmin(a, axis=None)
Minidx
Maxx = x.max()
Maxx
Maxidx = x.argmax()
Maxidx

#%% logical operators
np.all([True, True, False])
np.any([True, True, False])

# using for array comparisons
a = np. zeros((10,10))
np.any(a!=0)
np.all(a==a)

a = np.array([1,2,3,2])
b = np.array([2,2,3,2])
c = np.array([6,4,4,5])
((a<=b) & (b<=c)).all()

#%% Statistics
x = np.array([1,2,3,1])
y = np.array([[1,2,3], [5,6,1]])
x.mean()
np.median(x)
