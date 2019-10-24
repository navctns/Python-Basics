# -*- coding: utf-8 -*-
"""
Created on Wed May 29 22:13:52 2019

@author: naveen
"""

#Guess and check algorithm
#for determining the cube root
cube=int(input("Enter cube:"))#initialized
for guess in range(abs(cube)+1):#loop variant starts from 0
    if guess**3>=abs(cube):
        break
if guess**3!=abs(cube):
    print("It is not a perfect cube")
else:
    
    if cube<0:
        guess=-guess
    print("cube root of "+str(cube)+" is "+str(guess))