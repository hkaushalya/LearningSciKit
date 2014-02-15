# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 10:47:36 2014

@author: samantha
"""
class Point:
    class_x = 0
    class_y = 0
    
    def __init__(self, p, q):
        Point.class_x = p
        Point.class_y = q
        self.obj_x = p + 1
        self.obj_y = q + 1
        self.str = ''
        print 'Point.x/y:=', Point.class_x, ',', Point.class_y
        print 'self. x/y:=', self.obj_x, ',', self.class_x
        
        self.str = 'Class['+ str(Point.class_x) + ',' + str(Point.class_y) + '] '
        self.str += 'Obj [' + str(self.obj_x) + ',' + str(self.obj_y) + ']'
        
    def __str__(self):
        return self.str


p1 = Point(1,2)
p2 = Point(30,40)

str(p1)
str(p2)

p2.class_x = 2
p2.obj_x = 22
str(p2)

#print p1.x,',',p1.y
#print p1.a,',',p1.b
#print p2.x,',',p2.y


#[MCQ] Which of the following statement is not true?
#Point.x equals to 3 and Point.y equals to 4.
#Point.x equals to 1 and Point.y equals to 2.
#p1.x equals to 1 and p1.y equals to 2.
#p2.x equals to 2 and p2.y equals to 4.
#None of the above. 