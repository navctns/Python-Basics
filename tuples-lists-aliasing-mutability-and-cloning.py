# -*- coding: utf-8 -*-
"""
Created on Fri May 31 21:40:43 2019

@author: naveen
"""

#Tuples, lists,Aliasing,Mutability and cloning

#tuples-sequence of some things, immutable(not allowed to modify)
#
#te=() #empty tuple
#t=(2,"mit",3)#elements seperate by commas
#print t[0] #accessine elements with index with square brackets
#t=t+(5,6)#concatenating with another tuple
#print(t)
#
###slicing tuple
#print(t[1:2])#gives an extra comma, since tuple having ony one element
#print(t[1:3])
#print(t[1:4])
#print(t[1:5])
#print(t[1:6])

#print("length:",len(t))#gibes the length of the tuple
#t[1]=4#gives error,'tuple' object does not support item assignment

#tuple used to swap variable values
#x=int(input("enter x:"))
#y=int(input("enter y:"))
#print("x:",x)
#print("y:",y)
##swapping values of x and y
#(x,y)=(y,x)
#print("x-after swap:",x)
#print("y-after swap:",y)

##########################3333333
#In function it is only allowed to return one object, use tuple to return more than
#one value from a function
#example
def quotient_and_remainder(x,y):
    q=x//y
    r=x%y
    return (q,r)
    
print(quotient_and_remainder(5,2))

