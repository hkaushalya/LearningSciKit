# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 22:57:41 2014

@author: samantha
Refreshers using pyschool exercises
"""

def toString(alist):
    s = ''
    for i in alist:
        s += chr(i)
    
    return s
        
#print(toString([22,55,67]))

def BMI(weight, height):
	bmi = float(weight) / (height**2)
	s = "%.1f" % bmi
	return s

#print BMI(110,2)

def getSum(numList):
    n = 0
    for i in numList:
        s = str(i)
        l = len(s)
        c = s[l-1]
        n += int(c)
        print 's,l,c=', s,',',l,',',c
        
    return n
    
#print getSum([2,25])
#print getSum([23,32,54])
    
def isEquilateral(x, y, z):
    if (x<0 or y<0 or z<0):
        return False
    else:
        if (x == y and y==z and z==x):
            return True
        else:
            return False

print isEquilateral(-3,-3,-3)


def search(word, substring):
    i = word.find(substring)
    return i

def countVowels(word):
    
