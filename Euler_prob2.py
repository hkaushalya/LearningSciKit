# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 17:28:27 2014

@author: samantha
http://ivanidris.net/wordpress/index.php/2012/01/12/numpy-project-euler-problem-2

Uses the identity relation described in:
http://en.wikipedia.org/wiki/Fibonacci_number
"""

import numpy 

phi = (1 + numpy.sqrt(5))/2  # this is not the regular Pi!
print "phi = ", phi

n = numpy.log(4*10**6 *numpy.sqrt(5) + 0.05) /numpy.log(phi)
print n

n = numpy.arange(1,n)
print n

fib = (phi**n - (-1/phi)**n)/numpy.sqrt(5)
print "First 9 Fibonacci Numbers", fib[:9]

# convert to int (optional)
fib = fib.astype(int)
print "Integers", fib

# select even values numbers
eventerms = fib[fib%2 ==0]
print 'even terms:' , eventerms

print 'sum of even terms =', eventerms.sum()
