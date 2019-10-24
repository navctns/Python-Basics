# -*- coding: utf-8 -*-
"""
Created on Fri May 31 00:02:24 2019

@author: naveen
"""

#Function-The structure of a function
def is_even(i):
   
   #the specification, Docstring for a function, just like a user manual
    """
    input: i, positive int
    Returns True if number is even otherwise,False
   """
   #body of a function
    print("inside is_even")#for knowing the scope
    return i%2==0#Expression to evaluate and return
    
#inputting number
num=int(input("Enter the number:"))#inputting number, type castin to int since input() take it as string
res=is_even(num)#retrun is binded to a variable
if res==True:
    print(num,"is even !")
else:
    print(num,"is odd !")
        
#print(is_even(num))#because it returns as a boolean variable, shoud be printed to show it
#print(is_even(8))