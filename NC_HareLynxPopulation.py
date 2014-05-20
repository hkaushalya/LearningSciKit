# -*- coding: utf-8 -*-
"""
@author: samantha

Example: Data Statistics
Data downloaded from https://github.com/scipy-lectures/scipy-lecture-notes/tree/master/data
"""

#!cat data/populations.txt

# Load to np array
data = np.loadtxt('data/populations.txt')
# trcik: columns to variables
year, hares, lynxes, carrots = data.T
# plot
from matplotlib import pyplot as plt
plt.axes([0.2, 0.1, 0.5, 0.8])
plt.plot(year, hares, year, lynxes, year, carrots)
plt.legend(('Hare','Lynx','Carrot'), loc=(1.05, 0.5))

# mean population over time
populations = data[:, 1:]
populations.mean(axis=0)
# standard deviations
populations.std(axis=0)
# which species has the highest population each year?
np.argmax(populations, axis=1)