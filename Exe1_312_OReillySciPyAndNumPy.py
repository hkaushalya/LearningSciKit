# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 22:25:20 2014

@author: samantha
OReilly SciPy and Numpy
3.1.2 Solution to Functions

scipy.optimize.fsolve
"""

from scipy.optimize import fsolve
import numpy as np
import pylab as pl
#line = lambda x: x + 3
line = np.poly1d([1,-4,4]) #f=x^2-4x+x
line2 = np.poly1d([2,3],True) # f=(x-2)(x-3)
solution1 = fsolve(line,x0=0)
solution2 = fsolve(line2,x0=(1,5)) 
#ok. the root finding significantly depends on
# the guesses and how close the guesses are to the
# real! 


print np.poly1d(line), ': Roots->', solution1
print line2, ': Roots->', solution2

###=====================================
# finding intersection of two equations
###=====================================
# Defining function to simplify intersection solution
def findIntersection(func1, func2, x0):
    return fsolve(lambda x : func1(x) - func2(x), x0)

# Defining functions that will intersect
funky = lambda x : np.cos(x/5) * np.sin(x/2)
line = lambda x : 0.01 * x - 0.5

# Defining range and getting solutionson intersection points
x = np.linspace(0,45,10000)
results = findIntersection(funky, line,[15,20,30,35,40,45])

# print results
print ('\n --- Intersection points of funky and line: ---\n')
print(results, line(results))

pl.scatter(results, line(results), label='Intersection points',c='b',marker='D',s=100)
pl.plot(x,funky(x), color='red', label='Funky line')
pl.plot(x,line(x), color='green', label='Straight line')
pl.legend(('Funky line','Straight line', 'Intersection points'), loc='lower left', shadow=True)
pl.show()
savefig('FindIntersections.png')