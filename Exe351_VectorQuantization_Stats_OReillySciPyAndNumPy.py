# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 13:55:43 2014

@author: samantha
Vector Quantization
"""

import numpy as np
from scipy.cluster import vq
import pylab as pl

# Creating data
c1 = np.random.randn(100, 2) + 5
c2 = np.random.randn(30, 2) - 5
c3 = np.random.randn(50, 2)

# Pooling all the data into one 180 x 2 array
data =np.vstack([c1, c2, c3])


#print data
# Cluster centroids and variance from kmeans

centroids, variance = vq.kmeans(data,3)

#print 'centroids: ', centroids
#print 'variance: ', variance

# The 'identified' variable contains the information
# we need to seperate the points in clusters
# based on the vq function
identified, distance = vq.vq(data, centroids)

#print '\n identified: ', identified
#print '\n distance: ', distance

# Retrieving coordinates for points in each vq
# identified core

idx = identified
vqc1 = data[identified == 0,]
vqc2 = data[identified == 1,]
vqc3 = data[identified == 2,]

#pl.plot(data[idx==0,0],data[idx==0,1], 'orange')
#pl.plot(vqc2[0,:], 'green')
#pl.plot(vqc3[0], vqc3[1], 'blue')
#pl.plot(centroids[:,0],centroids[:,1],'sg',markersize=8)
#pl.show()
        