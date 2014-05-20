# -*- coding: utf-8 -*-
"""
@author: samantha
"""
import numpy as np
import matplotlib.pyplot as plt
image = np.random.rand(30, 30)
plt.imshow(image, cmap=plt.cm.hot)
plt.colorbar()

#%%
s= np.arange(0,56,1)
s.shape
s.ndim

#%% array creation
m = np.array([[1,2], [3,4]])  # a 2x2 matrix
m.shape
type(m)

n=np.array([[1,2,3], [4,5,6]])  # 2x3
n
n.shape
l=np.array([[1,2,3], [4,5,6],[7,8,9]])  # 3x3
l
l.shape


#%% intrinsic array creation
np.zeros((2,3))
np.arange(4,10,dtype=np.float)
np.linspace(1.0, 4.0, 6)  # break the space into 6 evenly spaced numbers
np.indices((3,3))
#%% indexing and slicing
s = np.arange(6) + np.arange(0,51,10)[:, np.newaxis]
s
s.shape
s[:,2]
s[0,3:5]
s[4:,4:]
s[2::2,0::2]
#s.reshape(3,6)

#%% Excercises pp.57
#exe1
a = (4,4)
a = np.ones(a, dtype=int)
a[3,1] = 6
a[2,3] = 2
a
a.shape
#exe2
#how to set offdiagnal elements along a diagonal line in a asymmetric matrix??
b= (6,5)
b = np.zeros(b, dtype=float)
b
di = np.diag(b,k=-1)
di

#exe3: using tile
a = (4,3)
b = (2,1)

tile
#%% tranposition
a = np.triu(np.ones((3,3)), 1)
a
a.T
b = a.T
a+b

#a += a.T #fails bcos a.T is a view!