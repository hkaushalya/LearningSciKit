# -*- coding: utf-8 -*-
"""
@author: samantha
3.4.2 Loading Data files
"""
import numpy as np
data = np.loadtxt('data/populations.txt')
data
np.savetxt('pop2.txt', data)