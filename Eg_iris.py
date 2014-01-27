# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:32:08 2014

@author: samantha
"""
# simple example shipped with the scikit: iris dataset
from sklearn import datasets

#%%
iris = datasets.load_iris()
data = iris.data
data.shape
iris.DESCR
#%%
### When the data is not initially in the (n_samples, n_features) shape,
###  it needs to be preprocessed in order to by used by scikit.

# An example of reshaping data would be the digits dataset

#%%
digits = datasets.load_digits()
digits.DESCR
digits.images.shape
#import pylab as pl
#for i in range(1,10):
#    figure(i)
#    pl.imshow(digits.images[i], cmap=pl.cm.gray_r)
#reshape data to use with scikit
data = digits.images.reshape((digits.images.shape[0], -1))

#%%
# Estimators objects
# Fitting data: the main API implemented by scikit-learn is that of the estimator. 
# An estimator is any object that learns from data; it may be a classification, 
# regression or clustering algorithm or a transformer that extracts/filters 
# useful features from raw data.
digits = datasets.load_digits()
digits.images.shape
data = digits.images.reshape((digits.images.shape[0], -1))

estimator.fit(data)

