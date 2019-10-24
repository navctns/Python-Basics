# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 19:03:48 2019

@author: naveen
"""

#OBJECT ORIENTED PROGRAMMING

#Everything in python is an object
#__init__used to initiate data
#defining a class , coordinate to represent a point in x-y plane
class coordinate(object):
     #initializing variables using special finction __init__
    def __init__(self,x,y):
        self.x=x
        self.y=y
    # For calculating the distance between two points
    def distance(self,other):
        x_diff_sq=(self.x-other.x)**2
        y_diff_sq=(self.y-other.y)**2
        return (x_diff_sq+y_diff_sq)*0.5
    #Another special method __str__ used to print datas in class
    #python calls the __str__ method when used with print on your class object
    #always returns a string
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"
    
        
#creating object of class
c=coordinate(3,4)
origin=coordinate(0,0)
#print(c.x)
#print(c.y)
#print(coordinate.distance(c,origin))#Accessing method in class, by class name
#print(c.distance(origin))#Accessing methods, by object, here by c
#print(c)
        
#Defining another class Fraction for fractional numbers

class Fraction(object):
    
    #initializing numerator and denomenator
    def __init__(self,num,denom):
        """numerator and denomenators are integers"""
        assert type(num)==int and type(denom)==int,"Values should be integers"
        self.num=num
        self.denom=denom
    def __str__(self):
        return str(self.num)+"/"+str(self.denom)
    #Addition of fractional numbers
    def __add__(self,other):
        top=self.num*other.denom+self.denom*other.num
        bott=self.denom*other.denom
        return Fraction(top,bott)
    #Subtraction
    def __sub__(self,other):
        top=self.num*other.denom-self.denom*other.num
        bott=self.denom*other.denom
        return Fraction(top,bott)
    def __float__(self):
        """Returns the float value of the Fraction"""
        return self.num/self.denom
    def inverse(self):
        """Returns the fraction representing the inverse of it"""
        return Fraction(self.denom,self.num)
a=Fraction(1,4)
b=Fraction(3,4)
c=a+b
print(a+b)
print(a-b)

print(Fraction.__float__(c))
print(float(b.inverse()))