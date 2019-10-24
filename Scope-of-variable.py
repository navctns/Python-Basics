# -*- coding: utf-8 -*-
"""
Created on Fri May 31 00:21:51 2019

@author: naveen
"""

#Scope of a variable

#the formal parameters gets bound to the value of actual parameters when function is called
#print("x(outside function)=",x)
#def f(x):#here x is the formal parameter, defined with funcion defnition
#    x=x+1
#    print("in f(x): x =",x)
#    return x
#x=3#having a global scope
#z=f(x)
#print("z =",z)
    

#Different conditions

##############################
#Not allowed in python, gives an error, "Unbounded local Error: Local variable referenced before assignment
def h(y):
    x+=1
x=5
h(x)
print x
