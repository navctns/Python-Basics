# -*- coding: utf-8 -*-
"""
Created on Wed May 29 22:53:47 2019

@author: naveen
"""

#initializing cube
cube=28
epsilon=0.01
num_guess=0
low=0
high=cube
guess=(low+high)/2.0
while abs(guess**3-cube)>=epsilon:
    if guess**3<cube:
        low=guess
    else:
        high=guess
    guess=(low+high)/2.0
    num_guess+=1
print "num_guess=",num_guess
print guess,"is close to the root of",cube