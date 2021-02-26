#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time      : 2021-02-26
# @Author    : ZedMoster1@gmail.com

class Polygon:
    '''多边形类'''
    
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for _ in range(no_of_sides)]
    
    def inputSides(self):
        self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in
                      range(self.n)]
    
    def dispSides(self):
        for i in range(self.n):
            print("Side", i + 1, "is", self.sides[i])


class Triangle(Polygon):
    '''三角形'''
    def __init__(self):
        # Polygon.__init__(self, 3)
        super().__init__(3)
    
    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('The area of the triangle is %0.2f' % area)


t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()
print("=" * 30)
print(isinstance(t, int))
print(isinstance(t, Triangle))
print(isinstance(t, Polygon))
print(isinstance(t, object))
