# -*- coding: utf-8 -*-
"""
@author: samantha
"""
import numpy as np
from scipy import io as spio
a = np.ones((3,3))
spio.savemat('file.mat', {'a':a})

#%%
print '2'
#%%
print "same"
#%%
r = ['red', 'blue', 'green', 'black', 'white', 'pink', 'purple']
print r
for i in r:
    print i
#%%
d = {'a': 1, 'b':1.2, 'c':1j}
for k,v in d.iteritems():
    print('%s %s'% (k, v))

for v in d.itervalues():
    print(v)
#%%
for x in [i**2 for i in range(4)]:

#%%
#[4*i**2/(4*i**2-1) for i in range(100)]
sum(range(4))
#%%
def variable_args(*args, **kwargs):
    print 'args is', args
    print 'kwargs is', kwargs

variable_args('one','two', x=1, y=2, z=3)

va = variable_args
va('three', x=1, y=2)

#%%
def funcname(params):
    """Concise one-line
    """
    pass

funcname?
#%%
# list inside a dictinary

dic = {'it1':[1,2], 'it2':[5], 'it3':[]}

for k,v in dic.iteritems():
    print k, v
    if iterable(v):
        v.append(666)
        for i in v:
            print i